from flask import request
import requests 
import random

import tmdb_client

from unittest.mock import Mock

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZjhhMzYyYWNjOTkyMmFjZjZmMDQyMjg0MWY5MDQyZCIsInN1YiI6IjYxZjk2Yjk3Y2NiMTVmMDBmYWY3YjZjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TXxYbka8zfyBryDlpse5tbyTG1GETiOrFqXYNIJwGNc"

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2