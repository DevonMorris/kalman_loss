PANDOC_OPTIONS=--standalone \
							 -V geometry:margin=1in \
							 -V linkcolor:blue \
							 --pdf-engine=xelatex \
							 -V mainfont="Liberation Sans" \
							 -V monofont="Liberation Mono" \
							 --highlight-style pygments.theme

pdfs = $(patsubst %.md, %.pdf,$(wildcard *md))

%.pdf : %.md
	pandoc $(PANDOC_OPTIONS) $< -o $@

docs: $(pdfs)

all : docs

.PHONY: all clean

clean:
	- rm -rf *.pdf
