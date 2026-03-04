"""Tests for rapid-dir-perms."""

import pytest
from rapid_dir_perms import perms


class TestPerms:
    """Test suite for perms."""

    def test_basic(self):
        """Test basic usage."""
        result = perms("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            perms("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = perms(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
