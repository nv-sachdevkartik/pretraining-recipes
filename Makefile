.PHONY: docs verify clean

docs:
	$(MAKE) -C docs current-docs

verify:
	$(MAKE) -C docs current-docs

clean:
	$(MAKE) -C docs clean
