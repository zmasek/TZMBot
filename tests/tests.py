# -*- coding: utf-8 -*-

"""Tests for `TZMBot` Discord app."""
import os
from unittest import mock

import asynctest
from tortoise import Tortoise
from TZMBot.cogs.biography import BiographyCog
from TZMBot.models import Biography
from TZMBot.settings import BASE_DIR

TEST_DB_PATH = os.path.join(BASE_DIR, '..', 'test_db.sqlite')
TEST_DB_URL = f"sqlite://{TEST_DB_PATH}"


class BasicTests(asynctest.TestCase):
    """Tests for `TZMBot` Discord app."""

    async def setUp(self):
        """Set up test database and a Biography cog."""
        mock_client = mock.MagicMock()
        self.biography = BiographyCog(mock_client)
        await Tortoise.init(db_url=TEST_DB_URL, modules={"models": ["TZMBot.models"]})
        await Tortoise.generate_schemas()

    async def tearDown(self):
        """Tear down test database."""
        await Tortoise.close_connections()
        os.remove(TEST_DB_PATH)

    async def test_get_bio(self):
        """Test get_bio method of Biography cog."""
        bio, _ = await Biography.get_or_create(person=456)
        bio.content = "Another user"
        await bio.save()
        result = await self.biography.get_bio(456)
        self.assertEqual(result, "Another user")

    async def test_set_bio(self):
        """Test set_bio command of Biography cog."""
        mock_ctx = mock.MagicMock()
        mock_ctx.author = mock.MagicMock()
        mock_ctx.author.id = 123
        await self.biography.set_bio.callback(
            self.biography, mock_ctx, member_bio="my bio"
        )
        result = await Biography.filter(person=123).first()
        self.assertEqual(result.content, "my bio")
