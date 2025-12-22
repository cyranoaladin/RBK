DOC=whitepaper/src/main.tex
OUTDIR=whitepaper/build
PDF=$(OUTDIR)/$(notdir $(DOC:.tex=.pdf))

.PHONY: build clean release

build:
	mkdir -p whitepaper/build && cd whitepaper/src && xelatex -interaction=nonstopmode -file-line-error -output-directory=../build main.tex && xelatex -interaction=nonstopmode -file-line-error -output-directory=../build main.tex || true

clean:
	rm -rf $(OUTDIR)

release:
	@[ -n "$(VERSION)" ] || { echo "VERSION manquante (ex: make release VERSION=4.0.0)"; exit 1; }
	mkdir -p releases
	cp $(PDF) releases/Livre_blanc_RBK_v$(VERSION).pdf

audit:
	@python3 -c 'import os; outfile = "whitepaper/full_source_audit.tex"; src_dir = "whitepaper/src"; files = [os.path.join(src_dir, "main.tex")] + sorted([os.path.join(src_dir, "chapters", f) for f in os.listdir(os.path.join(src_dir, "chapters")) if f.endswith(".tex")]) + [os.path.join(src_dir, "version.tex")]; open(outfile, "w").write("\n".join([f"\n% {"="*60}\n% START OF FILE: {f}\n% {"="*60}\n\n" + open(f).read() + f"\n\n% {"="*60}\n% END OF FILE: {f}\n% {"="*60}\n" for f in files if os.path.exists(f)])); print(f"Created {outfile}")'
