all: ghena.pdf www/ghena.html

ghena.pdf: ghena.tex *.bib
	pdflatex ghena.tex
	bibtex ghena
	pdflatex ghena.tex
	pdflatex ghena.tex

ghena: ghena.tex *.bib
	latex2html -split 0 -no_navigation -info 0 -image_type png ghena.tex

www/:
	mkdir -p www

www/ghena.html: ghena.tex *.bib www/
	htlatex ghena.tex "html" "" "-dwww/"
	bibtex ghena
	htlatex ghena.tex "html" "" "-dwww/"
	htlatex ghena.tex "html" "" "-dwww/"

clean:
	rm -f *.aux *.log *.pdf *.bbl *.blg
	rm -f *.4ct *.4tc *.css *.dvi *.html *.idv *.lg *.tmp *.xref
	rm -rf www/
	rm -rf ghena/

.PHONY: clean
