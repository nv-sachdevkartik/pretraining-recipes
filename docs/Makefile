# Minimal makefile for Sphinx documentation.

SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = .
BUILDDIR = _build

.PHONY: help current-docs linkcheck-local clean

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

current-docs:
	@rm -rf "$(BUILDDIR)/current"
	@$(SPHINXBUILD) -W --keep-going -b html "$(SOURCEDIR)" "$(BUILDDIR)/current" $(SPHINXOPTS)

linkcheck-local:
	@$(SPHINXBUILD) -W --keep-going -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck" $(SPHINXOPTS)

clean:
	@rm -rf "$(BUILDDIR)"
