# Configuration pour XeLaTeX
$pdf_mode = 1;
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape';
$out_dir = 'build';
$clean_ext = 'synctex.gz';

# Dépendances pour TikZ
add_cus_dep('tikz', 'pdf', 0, 'tikz2pdf');
sub tikz2pdf {
    my ($base_name, $path) = fileparse(@_[0]);
    my $source = "$path$base_name.tikz";
    my $target = "$path$base_name.pdf";
    return system("pdflatex -interaction=nonstopmode -output-directory=$out_dir '$source'");
}

# Surveiller les modifications
$preview_continuous_mode = 1;
$pdf_previewer = "start evince";
