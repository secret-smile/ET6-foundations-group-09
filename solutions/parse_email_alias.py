#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for parsing and validating email aliases.

Module contents:
    - parse_email_alias: validates and extracts components of an email alias

Created on 28 12 2024
@author: Mahdia Ahamdi
"""


def parse_email_alias(email: str) -> dict:
    """
    Parse and validate an email address with optional alias tags.

    Validates email format and extracts components including the local part,
    domain, and any alias tags. Supports Gmail-style + aliases and subdomain
    addresses.

    Parameters:
        email: str, the email address to parse

    Returns:
        dict containing:
            - valid: bool, whether the email is valid
            - local_part: str, part before the @ (None if invalid)
            - domain: str, part after the @ (None if invalid)
            - tags: list[str], any alias tags found (empty if none)
            - errors: list[str], any validation errors found

    Raises:
        AssertionError: if the input is not a string

    Examples:
        >>> # Test basic email
        >>> result = parse_email_alias("user@example.com")
        >>> result['valid']
        True
        >>> result['local_part']
        'user'
        >>> result['domain']
        'example.com'
        >>> result['tags']
        []

        >>> # Test with alias tag
        >>> result = parse_email_alias("user+tag@example.com")
        >>> result['valid']
        True
        >>> result['local_part']
        'user'
        >>> result['tags']
        ['tag']

        >>> # Test multiple tags
        >>> result = parse_email_alias("user+tag1+tag2@example.com")
        >>> result['tags']
        ['tag1', 'tag2']

        >>> # Test subdomain
        >>> result = parse_email_alias("user@sub.example.com")
        >>> result['domain']
        'sub.example.com'

        >>> # Test invalid email (no @)
        >>> result = parse_email_alias("invalid.email")
        >>> result['valid']
        False
        >>> 'Missing @ symbol' in result['errors']
        True

        >>> # Test empty local part
        >>> result = parse_email_alias("@domain.com")
        >>> result['valid']
        False
        >>> 'Empty local part' in result['errors']
        True

        >>> # Test invalid characters
        >>> result = parse_email_alias("user<>@domain.com")
        >>> result['valid']
        False
        >>> 'Invalid characters in local part' in result['errors']
        True

        >>> # Test missing TLD
        >>> result = parse_email_alias("user@sub.")
        >>> result['valid']
        False
        >>> 'Invalid domain (missing TLD)' in result['errors']
        True

        >>> # Test non-string input
        >>> parse_email_alias(12345)
        Traceback (most recent call last):
            ...
        AssertionError: Input must be a string
    """
    # defensive assertion
    assert isinstance(email, str), "Input must be a string"

    # Initialize result dictionary
    result = {
        "valid": False,
        "local_part": None,
        "domain": None,
        "tags": [],
        "errors": [],
    }

    # Basic validation for the input email
    if not email:
        result["errors"].append("Email cannot be empty")
        return result

    # Check for @ symbol
    if "@" not in email:
        result["errors"].append("Missing @ symbol")
        return result

    # Split into local part and domain
    local_part, domain = email.split("@", 1)

    # Validate local part
    if not local_part:
        result["errors"].append("Empty local part")
        return result

    # Check for invalid characters in local part
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789.!#$%&'*+-/=?^_`{|}~"
    )
    if not all(c in allowed_chars for c in local_part):
        result["errors"].append("Invalid characters in local part")
        return result

    # Extract tags if present
    base_local = local_part
    tags = []
    if "+" in local_part:
        base_local, *tags = local_part.split("+")

    # Validate domain
    if not domain:
        result["errors"].append("Empty domain")
        return result

    if ".." in domain:
        result["errors"].append("Invalid domain (consecutive dots)")
        return result

    domain_parts = domain.split(".")
    if len(domain_parts) == 1 or (len(domain_parts) > 1 and not domain_parts[-1]):
        result["errors"].append("Invalid domain (missing TLD)")
        return result

    if (
        not all(
            part and all(c.isalnum() or c == "-" for c in part)
            for part in domain_parts[:-1]
        )
        or not domain_parts[-1].isalnum()
    ):
        result["errors"].append("Invalid domain format")
        return result

    # If we got here, email is valid
    result["valid"] = True
    result["local_part"] = base_local
    result["domain"] = domain
    result["tags"] = tags

    return result
