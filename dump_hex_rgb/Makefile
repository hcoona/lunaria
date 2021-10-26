LIGHT_THEME=../lunaria-light.json
DARK_THEME=../lunaria-dark.json
ECLIPSE_THEME=../lunaria-eclipse.json

lunaria.ini: main.py $(LIGHT_THEME) $(DARK_THEME) $(ECLIPSE_THEME)
	python3 main.py > lunaria.ini

clean:
	$(RM) lunaria.ini

.PHONY: clean
