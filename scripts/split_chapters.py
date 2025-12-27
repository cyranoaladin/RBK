import os

def split_file():
    source_file = "Livre_blanc_v3.tex"
    output_dir = "chapters"
    os.makedirs(output_dir, exist_ok=True)

    with open(source_file, "r") as f:
        lines = f.readlines()

    # Define split points (start line 1-based, inclusive)
    # The end of one chapter is the start of the next - 1
    
    # Map of filename -> start_line (approximate from grep)
    chapter_starts = [
        ("01_vision.tex", 452),
        ("02_contexte.tex", 578),
        ("03_arbitrage.tex", 739),
        ("04_methodologie.tex", 887),
        ("05_structure.tex", 993),
        ("06_syllabus_tronc_commun.tex", 1080),
        ("07_soft_skills.tex", 1235),
        ("08_track_solana.tex", 1409),
        ("09_track_evm.tex", 1589),
        ("10_fiches_metiers.tex", 1713),
        ("11_capstones.tex", 1812),
        ("12_business_plan.tex", 1909),
        ("13_marketing.tex", 1967),
        ("14_risques.tex", 2015),
        ("15_roadmap.tex", 2042),
        ("16_token_reputation.tex", 2088),
        ("17_fiches_metiers_bis.tex", 2117),
        ("18_marketing_bis.tex", 2303),
        ("19_risques_bis.tex", 2394),
        ("20_roadmap_lancement.tex", 2507),
        ("21_differentiation.tex", 2616),
        ("22_conclusion.tex", 2707),
        ("annexe_a_syllabus_detaille.tex", 2863),
        ("annexe_b_finance.tex", 3582),
        ("annexe_c_juridique.tex", 3655),
        ("annexe_d_audit.tex", 3740),
        ("annexe_e_cockpit.tex", 3821),
        ("annexe_f_isa.tex", 3896),
        ("annexe_g_selection.tex", 4042),
        ("annexe_h_sbt.tex", 4137),
        ("annexe_i_dashboard.tex", 4229),
    ]

    # Pre-chapter content (Preamble + TOC)
    preamble_end = 451
    preamble_lines = lines[:preamble_end]
    
    # We will construct the new main file content start
    new_main_content = preamble_lines[:]

    # Loop through chapters to extract and write
    for i, (filename, start) in enumerate(chapter_starts):
        # Determine end line
        if i < len(chapter_starts) - 1:
            end = chapter_starts[i+1][1] - 1
        else:
            end = len(lines) # To the end of file

        # Adjust for 0-based indexing
        chunk = lines[start-1 : end]
        
        # Write chapter file
        with open(os.path.join(output_dir, filename), "w") as cf:
            cf.writelines(chunk)
            
        print(f"Created {filename} (Lines {start}-{end})")
        
        # Add input command to new main content
        new_main_content.append(f"\\input{{{output_dir}/{filename}}}\n")

    # Add end document if it was cut off (it likely is in the last chunk, but let's check)
    # Actually the last chunk goes to EOF, so it includes \end{document}
    # But usually we want the main file to control the document structure.
    # We should probably strip \end{document} from the last annex if we want to add it explicitly, 
    # but strictly inputting works fine if the last file has it.
    # Ideally, we want the main file to close the document.
    
    # Let's check if the last line of the last chunk is \end{document}
    last_chunk_name = chapter_starts[-1][0]
    
    # Write the new main file
    with open("Livre_blanc_v3_modular.tex", "w") as mf:
        mf.writelines(new_main_content)
    
    print("Created Livre_blanc_v3_modular.tex")

if __name__ == "__main__":
    split_file()
