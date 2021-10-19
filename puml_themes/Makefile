LUNARIZE=python3 ../lunarize.py
LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

all: puml-theme-lunaria-light.puml puml-theme-lunaria-dark.puml puml-theme-lunaria-eclipse.puml
clean:
	$(RM) puml-theme-lunaria-light.puml puml-theme-lunaria-dark.puml puml-theme-lunaria-eclipse.puml

puml-theme-lunaria-light.puml: template.puml $(LIGHT_THEME)
	$(LUNARIZE) --format=css_hex $(LIGHT_THEME) $< $@

puml-theme-lunaria-dark.puml: template.puml $(DARK_THEME)
	$(LUNARIZE) --format=css_hex $(DARK_THEME) $< $@

puml-theme-lunaria-eclipse.puml: template.puml $(ECLIPSE_THEME)
	$(LUNARIZE) --format=css_hex $(ECLIPSE_THEME) $< $@

.PHONY: all clean
