Rapport d'Analyse Approfondi : Programme RBK 2.0 – Niveau 1 (N1) "La Forge" & "Junior Web3 Builder"
1. Vision Stratégique et Architecture du Programme
1.1 Le Paradigme "Senior-by-Design" : Une Réponse à l'Obsolescence du Codeur Junior
L'industrie technologique traverse actuellement une mutation structurelle violente, catalysée par l'émergence des Grands Modèles de Langage (LLMs) tels que GPT-4 et Claude. Cette transformation rend le profil traditionnel du "développeur junior" économiquement obsolète, car la production de code syntaxique de base est désormais une commodité accessible à coût marginal nul. Face à ce constat, le programme RBK 2.0, et spécifiquement sa phase introductive Niveau 1 (N1) : La Forge, adopte une posture radicale : la formation d'Architectes Web3 plutôt que de simples codeurs.1
Cette phase de 12 semaines n'est pas conçue comme une simple introduction technique, mais comme un sas de décompression cognitive et physiologique. L'objectif est d'inculquer, dès les premiers jours, les réflexes et les standards d'un ingénieur senior. Là où les bootcamps classiques se concentrent sur la rapidité de déploiement via des abstractions de haut niveau (frameworks JavaScript, bibliothèques "magiques"), La Forge impose un retour aux fondamentaux systémiques. L'analyse des documents stratégiques révèle que cette approche vise à combler un "Skills Gap" critique sur le marché : la pénurie de talents capables de concevoir des systèmes distribués sécurisés, résilients et audités.1
Le terme "La Forge" n'est pas anodin ; il suggère un processus de transformation par la pression et la chaleur. Les apprenants sont immergés dans un environnement où la rigueur n'est pas optionnelle. La thèse centrale est que pour maîtriser les architectures Web3 complexes (Solana, EVM), un ingénieur doit d'abord maîtriser la machine elle-même. Cela se traduit par l'interdiction initiale des frameworks facilitants (comme Anchor sur Solana) au profit du développement natif en Rust, obligeant l'apprenant à comprendre la gestion manuelle de la mémoire, la sérialisation des données et les contraintes de calcul.1
1.2 La Méthodologie "Cyborg 2.0" : Intégration et Discipline de l'IA
Contrairement à une approche luddite qui rejetterait l'intelligence artificielle, RBK 2.0 embrasse le concept de l'ingénieur augmenté, ou "Cyborg". Cependant, l'intégration de ces outils durant le Niveau 1 est régie par des protocoles stricts pour éviter la dépendance précoce. L'analyse des supports pédagogiques indique une dichotomie intentionnelle :
La Phase "No-AI" (Piscine Rust) : Durant les premières semaines critiques, l'usage des assistants de code est restreint. L'objectif est neurologique : forcer le cerveau de l'apprenant à construire les modèles mentaux nécessaires à la résolution de problèmes complexes (gestion de l'ownership, borrow checker) sans béquille technologique.
L'Augmentation Progressive : Une fois les fondamentaux validés par des "Block Checks" rigoureux, l'IA est réintroduite non pas comme un générateur de solutions, mais comme un exosquelette de productivité. L'étudiant apprend à auditer le code généré par l'IA, à détecter les hallucinations de sécurité (telles que les "missing signer checks") et à orchestrer des composants complexes.1
Cette méthodologie répond directement à une menace existentielle pour les développeurs juniors : l'IA peut écrire du code, mais elle ne peut pas encore raisonner sur l'intention architecturale ou garantir la sécurité économique d'un protocole. Le "Junior Web3 Builder" sortant de La Forge est donc positionné non pas comme un exécutant, mais comme un vérificateur et un architecte de systèmes assisté par l'IA.
1.3 Métriques Opérationnelles et Économie de la Formation
La structure du Niveau 1 est conçue pour servir de filtre de qualité autant que de plateforme d'apprentissage. Les données financières et opérationnelles soulignent la sélectivité du programme :
Durée : 12 semaines intensives (S01–S12), représentant environ 480 à 600 heures de pratique délibérée.
Coût d'Entrée : Les frais de 2 900 TND pour ce niveau agissent comme un mécanisme de "skin in the game". Ce montant, bien qu'accessible comparé aux standards internationaux, est suffisamment élevé dans le contexte local pour filtrer les candidats peu engagés avant l'activation des mécanismes de financement plus complexes comme l'ISA (Income Share Agreement) aux niveaux supérieurs.1
Taux de Conversion Cible : Le programme anticipe et planifie un taux de passage de 70% du N1 vers le N2. Ce chiffre est révélateur : il admet explicitement que près d'un tiers de la cohorte ne survivra pas à l'exigence technique de La Forge, garantissant ainsi la densité de talent dans les phases ultérieures.1
Indicateur Clé
Valeur Cible
Justification Stratégique
Durée
12 Semaines
Temps nécessaire pour déconstruire les habitudes Web2 et reconstruire une mentalité Web3.
Technologie Socle
Rust
Langage à haute barrière d'entrée filtrant les profils sur leur capacité d'abstraction et de rigueur.
Format
Hybride / Présentiel Augmenté
Maximisation de la pression par les pairs (Peer Pressure) et du soutien communautaire.
Livrable de Sortie
NFT "Junior Web3 Builder"
Certification on-chain immuable prouvant la compétence technique (SBT).

2. Ingénierie Pédagogique : Les Quatre Piliers de La Forge
Le syllabus du Niveau 1 est structuré autour de quatre modules progressifs, chacun conçu pour briser une barrière cognitive spécifique et construire une compétence fondamentale. L'analyse détaillée des contenus révèle une progression logique allant du "Bas Niveau" (Gestion de la mémoire) vers le "Haut Niveau" (Architecture d'applications décentralisées).
2.1 Module 1 : Programmation Système & Fondamentaux Rust (Semaines 1-3)
Ce module constitue le "choc thermique" initial de La Forge. Il ne s'agit pas simplement d'apprendre la syntaxe d'un nouveau langage, mais de réapprendre à programmer en acceptant les contraintes physiques de la machine.
2.1.1 La Barrière de l'Ownership et du Borrowing
L'obstacle pédagogique majeur identifié dans l'enseignement de Rust est son modèle de gestion de la mémoire sans ramasse-miettes (Garbage Collector). Pour un développeur habitué à JavaScript ou Python, concepts dominants sur le marché, la gestion explicite de la mémoire est une compétence atrophiée. Le Module 1 attaque ce déficit frontalement.
L'analyse des ressources pédagogiques suggère l'utilisation intensive d'outils de visualisation pour démystifier ces concepts abstraits :
RustViz : Cet outil permet de générer des chronologies interactives montrant les événements d'emprunt (borrowing) et de possession (ownership) pour chaque variable. Plutôt que d'expliquer théoriquement pourquoi une variable ne peut pas être utilisée après un "move", RustViz montre graphiquement la fin de la durée de vie (lifetime) de la variable, offrant une représentation visuelle des règles invisibles du compilateur.3
RustOwl : Intégré dans l'IDE (VS Code), cet outil visualise les durées de vie et les mouvements de propriété directement dans le code source via des soulignements colorés. Cette rétroaction immédiate est cruciale pour la boucle d'apprentissage rapide visée par la méthode "Cyborg".6
2.1.2 Distinction Stack vs Heap
La compréhension physique de la mémoire est un prérequis pour l'optimisation des smart contracts sur Solana, où chaque octet et chaque unité de calcul (Compute Unit) compte. Le cursus force les étudiants à distinguer :
La Stack (Pile) : Rapide, taille fixe, LIFO. Utilisée pour les primitives et les pointeurs.
Le Heap (Tas) : Plus lent, dynamique, nécessite des pointeurs. Utilisé pour les vecteurs, les chaînes de caractères et les structures complexes.8
L'enseignement de ces concepts n'est pas théorique mais pratique : les étudiants doivent implémenter des structures de données qui manipulent explicitement ces zones mémoire, confrontant directement les erreurs de segmentation et les fuites de mémoire potentielles (bien que Rust les prévienne largement, comprendre pourquoi est l'objectif).
2.1.3 Projet Capstone M1 : Réimplémentation de ls
Pour valider cette phase, les apprenants ne réalisent pas des exercices abstraits mais reconstruisent des outils système fondamentaux. Le projet phare est la réécriture de la commande Unix ls (list directory contents) en Rust.
Ce projet impose la maîtrise de :
Appels Système : Interaction directe avec le noyau pour lire les métadonnées des fichiers.
Gestion des Erreurs : Utilisation idiomatique de Result<T, E> et Option<T> pour gérer les permissions refusées ou les fichiers manquants, remplaçant les mécanismes d'exception coûteux d'autres langages.
Parsing d'Arguments : Implémentation manuelle ou via des crates légères (comme clap ou structopt) de la logique de parsing des drapeaux CLI (-l, -a, --color), forçant une structuration rigoureuse des entrées utilisateur.10
2.2 Module 2 : Primitives Cryptographiques & Architecture Blockchain (Semaines 4-6)
Une fois la maîtrise du langage système acquise, La Forge pivote vers les mathématiques de la confiance. L'objectif est de démystifier la "magie" de la blockchain en obligeant les étudiants à construire ses primitives à partir de zéro.
2.2.1 Hachage et Arbres de Merkle
La compréhension profonde des structures de données immuables est essentielle. Les étudiants implémentent manuellement des fonctions de hachage (SHA-256) et construisent des Arbres de Merkle.
Pertinence Web3 : Les arbres de Merkle sont au cœur de la scalabilité de Solana (compression d'état) et des preuves d'inclusion pour les airdrops et les whitelists NFT. En codant un arbre de Merkle en Rust, les étudiants comprennent intrinsèquement comment vérifier l'intégrité d'un vaste ensemble de données avec une seule empreinte (racine).13
Incremental Merkle Trees : Pour les profils avancés, l'implémentation d'arbres incrémentaux (utilisés dans les protocoles de confidentialité comme Tornado Cash) introduit la notion de mise à jour d'état efficace on-chain.13
2.2.2 Cryptographie Asymétrique (Ed25519)
Contrairement à Ethereum qui utilise secp256k1, Solana repose sur la courbe Ed25519 pour ses signatures, privilégiant la performance et la sécurité. Le module couvre :
Génération de Paires de Clés : Utilisation des crates ed25519-dalek et rand pour générer des clés privées et publiques sécurisées.
Signatures Numériques : Implémentation de la logique de signature et de vérification off-chain. Cela permet aux étudiants de comprendre ce qui se passe réellement lorsqu'un utilisateur "signe" une transaction dans son portefeuille.16
Standard BIP-39 : Implémentation du standard de génération de phrases mnémoniques (seed phrases). Transformer de l'entropie binaire en mots humains est un exercice critique pour comprendre la sécurité des portefeuilles (Wallets).18
2.2.3 Projet Capstone M2 : Wallet CLI en Rust
Le livrable de cette phase est un portefeuille en ligne de commande (CLI Wallet) fonctionnel capable de :
Générer une phrase mnémonique sécurisée (BIP-39).
Dériver des paires de clés Ed25519 hiérarchiques.
Signer des messages arbitraires et vérifier ces signatures.
Ce projet ancre les concepts théoriques dans un outil utilisable, préfigurant les interactions complexes avec la blockchain.19
2.3 Module 3 : Développement Solana Natif (Semaines 7-9)
C'est ici que RBK 2.0 se distingue le plus nettement des autres formations. Au lieu de commencer par Anchor (le framework dominant qui simplifie le développement), le programme impose l'apprentissage du développement Natif (Raw Rust). C'est la philosophie de "L'Apprentissage par la Douleur" (Hard Fun).
2.3.1 Pourquoi le "Natif" d'abord?
Les frameworks comme Anchor abstraient des complexités critiques : la sérialisation des comptes, les vérifications de sécurité (discriminators), et la gestion des PDAs. En commençant par le natif, les étudiants apprennent :
Le Modèle de Compte : Comprendre que sur Solana, tout est un compte (programmes, données, système) et que les programmes sont apatrides (stateless).
Le Point d'Entrée Unique : Maîtriser la fonction process_instruction qui reçoit le program_id, les accounts, et les instruction_data sous forme brute.21
Sérialisation Manuelle (Borsh) : Implémentation explicite de Borsh (Binary Object Representation Serializer for Hashing) pour décoder les octets entrants. Cela inculque une conscience aiguë des coûts de calcul (Compute Units) liés à la désérialisation, souvent masqués par les macros d'Anchor.23
2.3.2 Program Derived Addresses (PDAs)
Le concept de PDA est souvent la bête noire des développeurs Solana débutants. En natif, les étudiants doivent calculer manuellement les "bump seeds" pour trouver des adresses hors de la courbe elliptique, permettant au programme de signer des transactions. Cette compréhension mathématique est indispensable pour éviter les vulnérabilités de sécurité liées aux collisions d'adresses ou aux accès non autorisés.25
2.3.3 Projet Capstone M3 : Compteur Décentralisé Natif
L'objectif est de déployer un programme sur le Devnet qui permet à des utilisateurs de créer un compteur (compte de données) et de l'incrémenter.
Contraintes : Interdiction d'utiliser Anchor. Utilisation explicite de solana_program::entrypoint.
Sécurité : L'étudiant doit implémenter manuellement les vérifications de signataire (is_signer) et de propriétaire (owner) du compte de données, des failles souvent exploitées dans les protocoles réels.2
2.4 Module 4 : Intégration Web3 & Architecture dApp (Semaines 10-12)
La dernière phase de La Forge connecte la logique on-chain (backend) à l'utilisateur final (frontend). Il ne s'agit pas de simple développement React, mais d'ingénierie d'interface pour systèmes distribués asynchrones.
2.4.1 Gestion de l'État Asynchrone
Les dApps doivent gérer l'incertitude du réseau. Les étudiants apprennent à gérer les états de transaction :
Processed : La transaction est traitée par un validateur.
Confirmed : Une majorité de validateurs a voté (finalité probable).
Finalized : La transaction est irréversible.
L'interface utilisateur doit refléter ces nuances pour éviter de tromper l'utilisateur (e.g., afficher un solde mis à jour avant la finalisation).28
2.4.2 Solana Wallet Adapter
L'intégration du Wallet Adapter dans une application React/Next.js est standardisée mais complexe. Les étudiants doivent :
Configurer les ConnectionProvider et WalletProvider pour gérer la persistance de la connexion.
Gérer les erreurs RPC (Remote Procedure Call) et implémenter des stratégies de basculement (failover) si un nœud RPC ne répond pas.30
Comprendre la différence entre "connecter un wallet" (lecture seule) et "signer une transaction" (action on-chain).
2.4.3 Projet Capstone Final N1 : La dApp Complète
La validation finale du Niveau 1 requiert la livraison d'une application complète (e.g., un système de vote ou un minter de tokens).
Stack : Programme Rust Natif + Frontend React + Intégration Wallet.
Critère de Réussite : Le système doit être déployé sur Devnet, documenté, et capable de gérer les erreurs courantes (fonds insuffisants, rejet de signature) sans crasher.1
3. Analyse de la Stack Technique et de l'Outillage
La sélection technologique pour le Niveau 1 est délibérément minimaliste et proche du métal ("bare metal") pour maximiser la compréhension.
3.1 Environnement de Développement (Le "Cockpit")
Langage : Rust (Stable channel). C'est l'outil exclusif pour la logique backend.
IDE : VS Code est recommandé, couplé impérativement à rust-analyzer. Ce dernier n'est pas vu comme un simple confort mais comme un outil pédagogique : ses infobulles sur les types inférés aident les étudiants à visualiser les transformations de données implicites.33
Terminal : L'usage d'un shell Unix (Bash/Zsh) est obligatoire. La navigation en ligne de commande pour compiler (cargo build), tester (cargo test) et déployer (solana program deploy) fait partie intégrante de la compétence "Systems Engineer".34
3.2 Outils de Visualisation et d'Analyse
Pour soutenir l'apprentissage cognitif difficile de l'ownership, des outils spécialisés sont intégrés :
RustViz : Utilisé dans les supports de cours pour générer des diagrammes SVG statiques et interactifs des durées de vie des variables. Cela permet aux étudiants de "voir" la mémoire.5
RustOwl : Extension expérimentale introduite pour visualiser en temps réel dans l'éditeur les emprunts et les déplacements de données, réduisant la boucle de feedback sur les erreurs de compilation.6
3.3 Stack Blockchain Native
Crates : solana-program (cœur), borsh (sérialisation), spl-token (interaction avec les tokens).
Infrastructure : solana-test-validator (blockchain locale) pour le cycle de développement rapide ("Hot Loop").
Client : @solana/web3.js (version 1.x ou 2.0 selon la stabilité au moment du cursus) pour l'interaction JavaScript. L'accent est mis sur la nouvelle API version 2.0 pour sa modularité et son "tree-shaking", préparant les étudiants aux standards futurs.35
4. Écosystème d'Évaluation et Certification
L'évaluation dans RBK 2.0 est continue, transparente et impitoyable sur la qualité. Elle repose sur le principe de la preuve de travail vérifiable.
4.1 Skill Mirror (Revue par les Pairs)
Inspiré de l'école 42 mais adapté, le rituel hebdomadaire "Skill Mirror" oblige chaque étudiant à auditer le code d'un pair.
Mécanisme : L'étudiant auditeur doit cloner le repo, exécuter les tests, et surtout, poser des questions sur les choix d'implémentation (ex: "Pourquoi as-tu utilisé Rc<RefCell<T>> ici?").
Objectif : Développer la capacité de lecture de code (Code Literacy) et l'argumentation technique. Si l'auteur ne peut pas justifier une ligne de code, le module est échoué, même si le code fonctionne.1
4.2 Block Checks (Jalons de Validation)
À la fin de chaque module (S3, S6, S9, S12), un examen formel appelé "Block Check" est organisé.
Nature : Épreuve pratique chronométrée en environnement contrôlé (souvent sans IA ou avec IA limitée).
Critères : Le code doit non seulement fonctionner (passer les tests unitaires) mais aussi respecter les standards de qualité (zéro warning clippy, formatage rustfmt).
Conséquence : L'échec à un Block Check bloque l'accès au module suivant, déclenchant une phase de remédiation ou, en cas d'échec répété, l'exclusion du cursus "Architecte" (réorientation possible vers des parcours moins intensifs).1
4.3 Certification SBT : "Junior Web3 Builder"
La réussite du Niveau 1 est sanctionnée non pas par un diplôme papier, mais par un Soulbound Token (SBT) émis sur la blockchain.
Technologie : NFT non transférable contenant dans ses métadonnées les hachages des projets validés (le ls clone, le Wallet CLI, le Native Program).
Valeur : Ce SBT agit comme une clé d'accès (Token Gating) pour le Niveau 2. Il prouve mathématiquement que le porteur a validé les compétences pré-requises, créant un standard de confiance pour les partenaires recruteurs dès la fin des 3 premiers mois.1
5. Synthèse des Modules et Livrables (Tableau Détaillé)
Le tableau suivant condense le parcours opérationnel de l'apprenant durant les 12 semaines de La Forge.
Semaine
Module / Thème
Concepts Techniques Clés (Deep Dive)
Outils & Crates
Livrable (Proof of Work)
S1-S3
Programmation Système
Ownership, Borrowing, Lifetimes, Stack vs Heap, Gestion d'erreurs (Result), Traits.
rustc, cargo, rustlings, clippy, clap
CLI ls Clone : Un outil ligne de commande reproduisant ls -la avec gestion des permissions et couleurs.
S4-S6
Crypto & Blockchain
Hachage (SHA256), Arbres de Merkle, Signatures Elliptiques (Ed25519), Entropie (BIP39).
sha2, ed25519-dalek, rand, hex, bip39
Rust Wallet CLI : Générateur de seed phrases et signataire de transactions offline.
S7-S9
Solana Natif
Statelessness, Account Model, PDAs (Seeds + Bump), Sérialisation Borsh manuelle, CPIs.
solana-program, borsh, solana-test-validator
Native Program : Compteur ou Memo on-chain déployé sur Devnet (Sans Anchor).
S10-S12
Intégration Web3
JSON-RPC, Wallet Adapters, Transaction Building, Gestion d'état Frontend.
web3.js (v2), @solana/wallet-adapter, React/Next.js
Full-Stack dApp : Interface React connectée au programme natif avec gestion d'erreurs UX.

6. Conclusion et Perspectives
Le Niveau 1 "La Forge" est conçu comme un creuset. En refusant la facilité des frameworks et en imposant une rigueur systémique via Rust, RBK 2.0 s'assure que les survivants de cette phase possèdent une plasticité mentale et une robustesse technique exceptionnelles. Ils ne sont pas encore des experts en DeFi ou en sécurité (objets du Niveau 2), mais ils possèdent les fondations inébranlables nécessaires pour le devenir. Ce pari sur l'exigence est la clé de la promesse "Senior-by-Design" : former non pas ceux qui utilisent les outils de demain, mais ceux qui sont capables de les construire.
Sources des citations
Livre_blanc_v5_landscape.pdf
Solana Security Risks, Issues & Mitigation Guide - Cantina.xyz, consulté le janvier 6, 2026, https://cantina.xyz/blog/securing-solana-a-developers-guide
RustEdu Workshop 2022 - RustViz: Interactively Visualizing Ownership and Borrowing, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=zCF8QVkc6IY
RustViz: Interactively Visualizing Ownership and Borrowing - University of Michigan, consulté le janvier 6, 2026, https://web.eecs.umich.edu/~comar/rustviz-hatra20.pdf
rustviz/rustviz-lifetimes: Interactively Visualizing Ownership and Borrowing for Rust - GitHub, consulté le janvier 6, 2026, https://github.com/rustviz/rustviz-lifetimes
Ownership and Lifetime Visualization Tool : r/rust - Reddit, consulté le janvier 6, 2026, https://www.reddit.com/r/rust/comments/1i8j7ti/ownership_and_lifetime_visualization_tool/
cordx56/rustowl: Visualize Ownership and Lifetimes in Rust - GitHub, consulté le janvier 6, 2026, https://github.com/cordx56/rustowl
The Stack and the Heap - The Rust Programming Language - MIT, consulté le janvier 6, 2026, https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/the-stack-and-the-heap.html
Memory Management in Rust: Stack vs. Heap - DEV Community, consulté le janvier 6, 2026, https://dev.to/iamdipankarpaul/memory-management-in-rust-stack-vs-heap-3m45
Recreating the "ls" Command-Line (CLI) Tool in Rust - YouTube, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=ZxFjbwmOaq4
Building a Custom Shell in Rust from scratch - DEV Community, consulté le janvier 6, 2026, https://dev.to/maxtaylor/custom-replshell-in-rust-550j
A Tiny `ls` Clone Written in Rust | Matthias Endler, consulté le janvier 6, 2026, https://endler.dev/2018/ls/
GitHub - sergerad/incremental-merkle-tree, consulté le janvier 6, 2026, https://github.com/sergerad/incremental-merkle-tree
Learning Rust - Merkle Tree - DEV Community, consulté le janvier 6, 2026, https://dev.to/msedzins/learning-rust-merkel-tree-9p
MakisChristou/merkle-rs: A Merkle tree implementation in Rust - GitHub, consulté le janvier 6, 2026, https://github.com/MakisChristou/merkle-rs
Generate Keypair using Ed25519 in Rust - SSOJet, consulté le janvier 6, 2026, https://ssojet.com/keypair-generation/generate-keypair-using-ed25519-in-rust/
ed25519 - crates.io: Rust Package Registry, consulté le janvier 6, 2026, https://crates.io/crates/ed25519
My first Rust project: a CLI tool to generate seed phrases for your Bitcoin wallet - Reddit, consulté le janvier 6, 2026, https://www.reddit.com/r/rust/comments/1lnco1i/my_first_rust_project_a_cli_tool_to_generate_seed/
Building a Bitcoin CLI Wallet in Rust - DEV Community, consulté le janvier 6, 2026, https://dev.to/_56d7718cea8fe00ec1610/building-a-bitcoin-cli-wallet-in-rust-3c48
Rust implementation of a helium wallet CLI - GitHub, consulté le janvier 6, 2026, https://github.com/helium/helium-wallet-rs
Developing Programs in Rust - Solana, consulté le janvier 6, 2026, https://solana.com/docs/programs/rust
Hello World | Solana, consulté le janvier 6, 2026, https://solana.com/id/developers/courses/native-onchain-development/hello-world-program
Borsh: A Comprehensive Guide and Its Role in Anchor for Solana | by Yong kang Chia, consulté le janvier 6, 2026, https://extremelysunnyyk.medium.com/borsh-and-its-role-in-anchor-for-solana-48c19308328f
Demystifying Borsh Serialization in Solana Programs: From TypeScript to Rust and Back, consulté le janvier 6, 2026, https://medium.com/@aswinsuriya16/demystifying-borsh-serialization-in-solana-programs-from-typescript-to-rust-and-back-7c6ee9daa44c
Program-Derived Address - Solana, consulté le janvier 6, 2026, https://solana.com/docs/core/pda
Solana School — Lesson 4 : Solana Programming Model II (Advanced CPI, PDA) with Hands-On Examples | by Sidarth S | Medium, consulté le janvier 6, 2026, https://medium.com/@sidarths/solana-school-lesson-4-solana-programming-model-ii-advanced-cpi-pda-with-hands-on-examples-d374506e4ad2
Rust Memory Safety on Solana: What Smart Contract Audits Reveal - Three Sigma, consulté le janvier 6, 2026, https://threesigma.xyz/blog/rust-and-solana/rust-memory-safety-on-solana
Transactions | Solana, consulté le janvier 6, 2026, https://solana.com/docs/core/transactions
Solana Data Analytics 101: An Intro to Tokens, Transfers, and Balances - YouTube, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=cr9nMEoxP18
How to Connect a Wallet with React - Solana, consulté le janvier 6, 2026, https://solana.com/developers/cookbook/wallets/connect-wallet-react
How to Connect Users to Your dApp with the Solana Wallet Adapter and Scaffold, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/dapps/how-to-connect-users-to-your-dapp-with-the-solana-wallet-adapter-and-scaffold
How to Deploy Solana Frontend: Step by Step Guide, consulté le janvier 6, 2026, https://www.bu.edu/housing/wp-content/themes/r-housing/js/vendor/pannellum/pannellum.htm?config=/\/anni.ie/cf/09dc596511ed3e5
How to Learn Rust in 2025: A Complete Beginner's Guide to Mastering Rust Programming, consulté le janvier 6, 2026, https://blog.jetbrains.com/rust/2024/09/20/how-to-learn-rust/
Visualizing memory layout of Rust's data types - YouTube, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=7_o-YRxf_cc
How to Start Building with the Solana Web3.js 2.0 SDK - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/how-to-start-building-with-the-solana-web3-js-2-0-sdk
Web3 Beginner Series: Upgrade @solana/web3.js 2.x Now To Use Functional Programming, consulté le janvier 6, 2026, https://medium.com/@zan.top/web3-beginner-series-upgrade-solana-web3-js-2-x-now-to-use-functional-programming-cb9f85e6d332

