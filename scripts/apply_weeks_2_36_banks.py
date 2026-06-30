#!/usr/bin/env python3
"""Apply premium intermediate/advanced/expert banks for weeks 2–36."""

from apply_handcrafted_premium_qa import (
    splice_week_advanced,
    splice_week_expert,
    splice_week_intermediate,
    _bank_tier,
)
from premium_qa_data_weeks_02_07_banks import ALL_WEEKS_02_07_BANKS
from premium_qa_data_weeks_08_17_20_banks import ALL_WEEKS_08_17_20_BANKS
from premium_qa_data_weeks_09_16_banks import ALL_WEEKS_09_16_BANKS
from premium_qa_data_weeks_21_28_banks import ALL_WEEKS_21_28_BANKS
from premium_qa_data_weeks_29_36_banks import ALL_WEEKS_29_36_BANKS

ALL_WEEKS_2_36_BANKS = {
    **ALL_WEEKS_02_07_BANKS,
    **ALL_WEEKS_08_17_20_BANKS,
    **ALL_WEEKS_09_16_BANKS,
    **ALL_WEEKS_21_28_BANKS,
    **ALL_WEEKS_29_36_BANKS,
}


def main() -> None:
    total = 0
    for week in sorted(ALL_WEEKS_2_36_BANKS.keys()):
        banks = ALL_WEEKS_2_36_BANKS[week]
        splice_week_intermediate(week, _bank_tier(banks, "intermediate"))
        splice_week_advanced(week, _bank_tier(banks, "advanced"))
        splice_week_expert(week, _bank_tier(banks, "expert"))
        total += 90
    print(f"Done — weeks 2–36 banks applied ({len(ALL_WEEKS_2_36_BANKS)} weeks, {total} questions)")


if __name__ == "__main__":
    main()
