def allows_internet_egress(profile: str) -> bool:
    return profile in {"edge", "nat"}