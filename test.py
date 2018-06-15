#!/usr/bin/env python
"""Tests for all modules of the SET solver."""

import os
import shutil
import unittest
from common import IM_DATA_DIR
import card_finder as cf
import classify_card as cc

TMP_DIR = 'tmp'
TEST_DATA_DIR = os.path.join(IM_DATA_DIR, 'test')

class TestAll(unittest.TestCase):

  def rm_tmp(self):
    if os.path.exists(TMP_DIR):
      shutil.rmtree(TMP_DIR)

  def setUp(self):
    self.rm_tmp()

  def tearDown(self):
    self.rm_tmp()

  def test_card_finder_e2e(self):
    game_num = 7
    card_count = 12
    game_file = cf.game_img_filename(game_num)

    cards = list(cf.find_cards(game_file))
    self.assertEqual(len(cards), card_count)

    cf.write_cards(cards, out_dir=TMP_DIR)
    self.assertEqual(len(os.listdir(TMP_DIR)), card_count)

  def test_classify_card_e2e(self):
    # this will break if classify_card() is modified to return something
    # other than the nearest labeled card filename
    card_file = os.path.join(TEST_DATA_DIR, 'card06.jpg')
    expected_label = 'purple-triple-solid-capsule.jpg'

    self.assertEqual(
      cc.classify_card(card_file),
      expected_label
    )

if __name__ == "__main__":
  unittest.main()
