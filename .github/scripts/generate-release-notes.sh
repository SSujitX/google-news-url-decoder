#!/usr/bin/env bash
# Build categorized GitHub Release notes from conventional commits.
# Usage:
#   ./generate-release-notes.sh [PREV_TAG] [NEW_TAG] [BUMP] [FROM_VER] [TO_VER]
set -euo pipefail

PREV_TAG="${1:-}"
NEW_TAG="${2:-}"
BUMP="${3:-}"
FROM_VER="${4:-}"
TO_VER="${5:-}"

REPO_SLUG="${GITHUB_REPOSITORY:-SSujitX/google-news-url-decoder}"
SERVER_URL="${GITHUB_SERVER_URL:-https://github.com}"
COMMIT_BASE="${SERVER_URL}/${REPO_SLUG}/commit"
VER="${TO_VER:-${NEW_TAG#v}}"

if [[ -n "$PREV_TAG" ]]; then
  RANGE="${PREV_TAG}..HEAD"
else
  RANGE="HEAD"
fi

mapfile -t COMMITS < <(git log "$RANGE" --pretty=format:'%s%x09%h%x09%H' --no-merges)

feat=()
fix=()
perf=()
refactor=()
test=()
docs=()
build=()
ci=()
chore=()
other=()

for line in "${COMMITS[@]+"${COMMITS[@]}"}"; do
  [[ -n "$line" ]] || continue
  subject="${line%%$'\t'*}"
  rest="${line#*$'\t'}"
  short="${rest%%$'\t'*}"
  full="${rest#*$'\t'}"
  if [[ "$subject" =~ ^chore\(release\): ]]; then
    continue
  fi
  entry="- ${subject} ([${short}](${COMMIT_BASE}/${full}))"
  if [[ "$subject" =~ ^(feat)(\(.+\))?\!?: ]]; then
    feat+=("$entry")
  elif [[ "$subject" =~ ^(fix)(\(.+\))?\!?: ]]; then
    fix+=("$entry")
  elif [[ "$subject" =~ ^(perf)(\(.+\))?\!?: ]]; then
    perf+=("$entry")
  elif [[ "$subject" =~ ^(refactor)(\(.+\))?\!?: ]]; then
    refactor+=("$entry")
  elif [[ "$subject" =~ ^(test)(\(.+\))?\!?: ]]; then
    test+=("$entry")
  elif [[ "$subject" =~ ^(docs)(\(.+\))?\!?: ]]; then
    docs+=("$entry")
  elif [[ "$subject" =~ ^(build)(\(.+\))?\!?: ]]; then
    build+=("$entry")
  elif [[ "$subject" =~ ^(ci)(\(.+\))?\!?: ]]; then
    ci+=("$entry")
  elif [[ "$subject" =~ ^(chore|style)(\(.+\))?\!?: ]]; then
    chore+=("$entry")
  else
    other+=("$entry")
  fi
done

emit_section() {
  local title="$1"
  shift
  local -a items=("$@")
  if [[ "${#items[@]}" -eq 0 ]]; then
    return 0
  fi
  echo "### ${title}"
  echo
  printf '%s\n' "${items[@]}"
  echo
}

echo "## googlenewsdecoder ${NEW_TAG}"
echo
if [[ -n "$BUMP" && -n "$FROM_VER" && -n "$TO_VER" ]]; then
  if [[ "$FROM_VER" == "$TO_VER" ]]; then
    echo "Semantic bump: **${BUMP}** (version unchanged at \`${TO_VER}\`)."
  else
    echo "Semantic bump: **${BUMP}** to \`${TO_VER}\`."
  fi
  echo
fi
if [[ -n "$PREV_TAG" ]]; then
  echo "[Compare with ${PREV_TAG}](${SERVER_URL}/${REPO_SLUG}/compare/${PREV_TAG}...${NEW_TAG})"
  echo
else
  echo "Initial tagged release."
  echo
fi

emit_section "Features" "${feat[@]+"${feat[@]}"}"
emit_section "Fixes" "${fix[@]+"${fix[@]}"}"
emit_section "Performance" "${perf[@]+"${perf[@]}"}"
emit_section "Documentation" "${docs[@]+"${docs[@]}"}"
emit_section "Tests" "${test[@]+"${test[@]}"}"
emit_section "Refactoring" "${refactor[@]+"${refactor[@]}"}"
emit_section "CI" "${ci[@]+"${ci[@]}"}"
emit_section "Build" "${build[@]+"${build[@]}"}"
emit_section "Maintenance" "${chore[@]+"${chore[@]}"}"
emit_section "Other" "${other[@]+"${other[@]}"}"

if [[ ${#feat[@]} -eq 0 && ${#fix[@]} -eq 0 && ${#perf[@]} -eq 0 && ${#refactor[@]} -eq 0 && ${#test[@]} -eq 0 && ${#docs[@]} -eq 0 && ${#build[@]} -eq 0 && ${#ci[@]} -eq 0 && ${#chore[@]} -eq 0 && ${#other[@]} -eq 0 ]]; then
  echo "No new conventional commits since the previous release."
  echo
fi

echo "---"
echo
echo "**PyPI:** https://pypi.org/project/googlenewsdecoder/${VER}/"
echo
echo "\`pip install googlenewsdecoder==${VER}\` or \`uv add googlenewsdecoder==${VER}\`"
echo
echo "**Docs:** ${SERVER_URL}/${REPO_SLUG}#readme"
