all: ghena.pdf www/ghena.html ../cv.tar.gz

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

../cv.tar.gz: ghena.pdf www/ghena.html
	cd ../ && tar -czf cv.tar.gz cv/

clean:
	rm -f *.aux *.log *.pdf *.bbl *.blg
	rm -f *.4ct *.4tc *.css *.dvi *.html *.idv *.lg *.tmp *.xref
	rm -rf www/
	rm -rf ghena/
	rm -f ../cv.tar.gz

.PHONY: clean
