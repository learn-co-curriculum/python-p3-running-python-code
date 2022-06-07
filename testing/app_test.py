#!/usr/bin/env python

from logging import captureWarnings
from os import path
import runpy
import io
import sys

def test_app_py_exists():
    assert(path.exists("app.py"))

def test_app_py_runs():
    runpy.run_path("app.py")

def test_prints_hello_world():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    runpy.run_path("app.py")
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == "Hello World! Pass this test, please.\n")
