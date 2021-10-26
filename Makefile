TOPTARGETS := all clean
SUBDIRS := css dump_hex_rgb gogh kitty qterminal tmtheme vscode winterminal xrdb

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
