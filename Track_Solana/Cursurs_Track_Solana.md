Rapport Stratégique de Déploiement Opérationnel : Architecture Curriculaire et Infrastructurelle du Track Solana RBK 2.0 (Studio "Senior-by-Design")
1. Synthèse Exécutive et Alignement Stratégique
La transformation de ReBootKamp (RBK) vers sa version 2.0 marque une rupture fondamentale avec les modèles éducatifs conventionnels de type "bootcamp". En adoptant le paradigme du "Web3 Build Studio" et une architecture pédagogique bi-modale (EVM & Solana), RBK ne se contente plus de former des développeurs juniors, mais forge des "Architectes de la Souveraineté Numérique".1 Ce rapport constitue le document de référence, le "Master Blueprint", pour la production de l'intégralité des ressources pédagogiques, techniques et infrastructurelles nécessaires au déploiement du Track Solana et du volet Validator Architect.
L'analyse approfondie du Livre Blanc RBK 2.0 et des tendances technologiques de 2025 révèle une exigence critique : le marché ne valorise plus la simple production de code syntaxique, désormais commoditisée par l'intelligence artificielle générative. La valeur s'est déplacée vers la conception de systèmes résilients, l'audit de sécurité et l'opérationnalisation d'infrastructures critiques.1 Par conséquent, ce rapport détaille une stratégie de formation "Senior-by-Design", où chaque module est conçu pour simuler les contraintes de production d'un environnement mainnet à haute fréquence.
1.1 La Thèse "Senior-by-Design" appliquée à Solana
L'écosystème Solana, avec son modèle de programmation sans état (stateless) et sa machine virtuelle haute performance (SVM), impose une rigueur technique supérieure à celle de l'écosystème EVM classique. Pour RBK 2.0, cela implique une trajectoire pédagogique spécifique :
De la Syntaxe à la Sûreté Mémoire : L'apprentissage de Rust ne se limite pas à la syntaxe ; il doit ancrer les concepts d'Ownership et de Borrowing comme mécanismes fondamentaux de sécurité financière.2
Du Codeur au "Guardian" : Le profil de sortie n'est pas seulement un constructeur, mais un auditeur. La sécurité n'est pas un module final, mais une pratique transversale intégrée dès le premier jour via des outils comme Trident et Soteria.3
De l'Utilisateur à l'opérateurl'Opérateur : La compréhension de l'infrastructure physique (Validateurs, RPC, MEV) est indispensable pour architecturer des protocoles performants. Le "Validator Track" n'est donc pas une option périphérique, mais une composante structurelle de l'excellence technique.1
1.2 Méthodologie "Cyborg 2.0" : L'Ingénierie Augmentée
Le rapport intègre pleinement la méthodologie "Cyborg" prescrite par le manifeste RBK. L'utilisation d'assistants IA (GitHub Copilot, Cursor) est obligatoire mais encadrée par le principe "Don't Trust, Verify". L'ingénieur RBK doit être capable de générer du code à haute vitesse via l'IA, mais surtout de le vérifier formellement, de l'optimiser pour les unités de calcul (Compute Units) et de le sécuriser contre les vecteurs d'attaque sophistiqués.1
2. Architecture Détaillée du Cursus (48 Semaines)
Le programme est structuré en trois niveaux progressifs (N1, N2, N3), totalisant 48 semaines d'immersion intensive. Cette structure permet une filtration rigoureuse des talents suivie d'une spécialisation profonde.
2.1 Niveau 1 (N1) : La Forge & "Junior Web3 Builder" (Semaines 1–12)
Objectif Stratégique : Cette phase agit comme le filtre principal ("La Piscine"). Elle vise à établir des fondations inébranlables en programmation système (Rust) et en primitives cryptographiques, sans l'assistance de frameworks de haut niveau comme Anchor. L'objectif est de comprendre le "comment" avant d'utiliser le "pourquoi".
Module 1.1 : Fondamentaux Rust & Programmation Système (S1-S3)
Ce module est conçu pour briser les habitudes de programmation permissive (comme en JavaScript ou Python) et imposer la rigueur de la gestion mémoire manuelle.
Contenu Détaillé :
Gestion Mémoire : Stack vs Heap. Comprendre pourquoi Solana privilégie l'allocation sur la Stack pour des raisons de performance et de déterminisme.7
Ownership & Borrowing : Maîtrise absolue du Borrow Checker. Comprendre les règles de mutabilité et les lifetimes, essentiels pour manipuler les AccountInfo de Solana sans provoquer de comportements indéfinis.
Types & Traits : Utilisation avancée des Enums (pour les instructions), des Traits (pour la sérialisation) et des génériques.
Concurrence : Introduction aux primitives de concurrence, préparant le terrain pour le modèle d'exécution parallèle Sealevel de Solana.
Livrables Attendus :
Une implémentationréimplémentation partielle de commandes Unix (comme ls ou grep) en Rust pour prouver la maîtrise des E/S et de la mémoire.
Validation des exercices "Rustlings" à 100% avec zéro warning Clippy.8
Module 1.2 : Cryptographie & Primitives Blockchain (S4-S6)
Avant de toucher à un smart contract, l'étudiant doit comprendre ce qui sécurise le réseau.
Contenu Détaillé :
Signatures Numériques : Implémentation manuelle de la vérification de signatures Ed25519. Comprendre la relation mathématique entre clé privée et clé publique.
Hashing & Merkle Trees : Construction d'un arbre de Merkle pour comprendre comment Solana vérifie l'état et les transactions (Proof of History).
Structure de donnéesDonnées : Analyse binaire d'une transaction Solana (Header, Account Keys, Recent Blockhash, Instructions).
Livrables Attendus :
Un portefeuille CLI (Command Line Interface) capable de générer des paires de clés, de signer des messages et de vérifier des signatures hors-chaîne.1
Module 1.3 : Développement "Native Rust" & Modèle de Compte (S7-S9)
L'interdiction temporaire du framework Anchor force l'étudiant à interagir avec le runtime Solana à bas niveau.
Contenu Détaillé :
Le Point d'Entrée : Maîtriser la fonction process_instruction unique et le décodage manuel des données d'instruction (Instruction Data).
Sérialisation Borsh : Utilisation de la bibliothèque Borsh pour sérialiser et désérialiser les états de compte. Comprendre le coût en Compute Units (CU) de la sérialisation.7
Modèle de Compte : Distinction entre Comptes Exécutables (Programmes) et Comptes de Données. Le concept de "Rent" (Loyer) et d'exemption de loyer.
Program Derived Addresses (PDA) : Calcul manuel des adresses dérivées (find_program_address) et gestion des "Bumps" pour assurer le déterminisme.9
Livrables Attendus :
Un programme de "Compteur" distribué écrit en Rust pur, déployé sur Devnet, capable d'incrémenter une valeur stockée dans un PDA.10
Module 1.4 : Intégration Web3 & CI/CD (S10-S12)
La connexion entre le monde off-chain et on-chain.
Contenu Détaillé :
Solana Web3.js 2.0 : Utilisation de la nouvelle API JavaScript pour construire et envoyer des transactions.
Wallet Adapters : Intégration de Phantom et Solflare dans une dApp React. Gestion des erreurs de connexion et de signature.
Pipelines CI/CD : Configuration de GitHub Actions pour compiler le programme Rust et exécuter les tests unitaires à chaque Pull Request.1
Livrables Attendus :
Une mini-dApp complète (Frontend + Programme Natif) permettant de créer et lire des messages on-chain. Validation du "Block Check N1" pour le passage au niveau supérieur.
2.2 Niveau 2 (N2) : "Web3 Engineer" - Spécialisation Track A (Semaines 13–28)
Objectif stratégiqueStratégique : Passer de la compréhension fondamentale à la productivité industrielle. L'introduction du framework Anchor et des standards Token-2022 permet de construire des applications complexes, sécurisées et conformes aux standards 2025.
Module 2.1 : Maîtrise du Framework Anchor & IDL (S13-S16)
Anchor est le "Rails" de Solana, mais il ne doit pas être une "boîte noire".
Contenu Détaillé :
Macros & Attributs : Dissection des macros #[program], #[derive(Accounts)] et #[account]. Comment elles génèrent le code de vérification de sécurité (Ownership, Signer checks).11
Interface Definition Language (IDL) : Comment l'IDL est généré et utilisé pour créer des clients TypeScript typés automatiquement.
Tests TypeScript : Écriture de suites de tests complètes en utilisant @coral-xyz/anchor. Mocking des comptes et simulation de scénarios d'échec.12
Gestion des Erreurs : Définition d'erreurs personnalisées (ErrorCode) et utilisation de la macro require! pour des assertions élégantes.
Lab "Twitter on Solana" : Développement d'un réseau social décentralisé. Implémentation de structures de données relationnelles (Tweets liés à un User Profile PDA) et filtrage via instructions discriminantes.
Module 2.2 : Architecture Avancée & Composabilité (S17-S20)
Solana brille par sa composabilité. Ce module enseigne comment les programmes interagissent entre eux.
Contenu Détaillé :
Cross-Program Invocations (CPI) : Appel de programmes externes (System Program, Token Program) depuis un smart contract. Utilisation de CpiContext et propagation des signatures.13
Signature par PDA : Le mécanisme invoke_signed qui permet à un programme de signer une transaction au nom d'un PDA qu'il contrôle (Seeds + Bump). C'est la base des Vaults et des Escrows.15
Pattern "Master-Slave" : Conception d'architectures où un programme central contrôle plusieurs sous-comptes ou sous-programmes, essentiel pour les protocoles DeFi complexes.14
Lab "Escrow Décentralisé" : Création d'un contrat d'échange atomique (Atomic Swap). Le programme doit détenir des fonds dans un PDA (Vault) et ne les libérer que si deux parties satisfont les conditions d'échange.16
Module 2.3 : Standards Token-2022 & Finance Programmable (S21-S24)
Le standard Token-2022 (Token Extensions) redéfinit la tokenomie sur Solana.
Contenu Détaillé :
Transfer Hooks : Implémentation de logique arbitraire exécutée à chaque transfert de token. Cas d'usage : Enforceurs de redevances NFT, Listes blanches KYC pour les actifs régulés (RWA).18
Frais de Transfert (Transfer Fees) : Configuration de taxes protocolaires natives, prélevées automatiquement lors des transferts.20
Transferts Confidentiels : Utilisation des preuves à divulgation nulle de connaissance (ZK Proofs) pour masquer les montants de transaction, une fonctionnalité clé pour l'adoption institutionnelle.21
Métadonnées On-Chain : Utilisation des pointeurs de métadonnées pour stocker les attributs des actifs directement sur la chaîne ou via des pointeurs immuables.22
Lab "RWA Stablecoin" : Lancement d'un stablecoin conforme (Compliant) qui utilise des Transfer Hooks pour bloquer les transactions vers des adresses sanctionnées et prélève des frais de gestion.
Module 2.4 : Sécurité Offensive & Durcissement (S25-S28)
Préparation au rôle de "Guardian". L'étudiant apprend à penser comme un attaquant.
Contenu Détaillé :
Vecteurs d'Attaque Solana : Ré-entrance (via CPI), validation manquante de l'appartenance des comptes, attaques par substitution de compte, débordements arithmétiques.23
Fuzz Testing avec Trident : Utilisation du framework Trident pour générer des millions d'entrées aléatoires et tester les invariants du programme. Découverte de bugs de logique invisibles aux tests unitaires.3
Analyse Statique avec Soteria : Intégration de scanners de vulnérabilités dans le flux de travail pour détecter les erreurs courantes avant la revue de code.4
Lab "Capture The Flag (CTF)" : Les étudiants reçoivent des contrats vulnérables (honeypots) et doivent écrire des scripts d'exploitation pour drainer les fonds, puis proposer les correctifs (patches).
2.3 Niveau 3 (N3) : "Web3 Architect" & Studio de Production (Semaines 29–48)
Objectif Stratégique : Excellence opérationnelle et infrastructurelle. Ce niveau forme les véritables architectes capables de déployer, maintenir et sécuriser des réseaux et des protocoles majeurs.
Module 3.1 : Le Validator Architect & Infrastructure (S29-S34)
Ce module distingue RBK 2.0 des autres formations. L'architecte doit maîtriser le "métal" sur lequel tourne le code.
Contenu Détaillé :
Hardware & Bare Metal : Spécifications précises pour les validateurs Mainnet (CPU AMD EPYC haute fréquence, 256GB+ RAM ECC, Disques NVMe en RAID). Comprendre l'impact du matériel sur la latence de vote.5
Diversité des Clients : Installation et configuration comparée des clients Agave (Solana Labs) et Jito-Solana (Optimisé MEV). Introduction à l'architecture de Firedancer (C++) et ses implications pour la performance réseau.27
MEV & Jito Bundles : Fonctionnement du moteur de blocs Jito, configuration d'un Relayer, et stratégies d'optimisation des revenus via les pourboires (tips) MEV.29
Monitoring & Observabilité : Mise en place de la stack TIG (Telegraf, InfluxDB, Grafana). Création de tableaux de bord pour surveiller le "Skip Rate", la "Vote Latency" et l'état de délinquance.31
Lab "Testnet Validator" : Chaque étudiant déploie un validateur sur le Testnet Solana, le maintient en ligne pendant 2 semaines, configure le monitoring et simule une procédure de mise à jour sans downtime (failover).
Module 3.2 : Audit Avancé & Réponse aux Incidents (S35-S40)
La production de rapports d'audit de niveau professionnel.
Contenu Détaillé :
Modélisation des Menaces (Threat Modeling) : Application de méthodologies (comme STRIDE) aux protocoles DeFi. Identifier les actifs critiques et les surfaces d'attaque.1
Rapport d'Audit : Rédaction de rapports standardisés classifiant les risques (Critique, Haut, Moyen, Bas, Info) avec preuves de concept (PoC) exploitables.1
War Room & Gestion de Crise : Simulation d'incidents de sécurité en temps réel. Procédures de mise en pause de protocole (Circuit Breakers), migration de liquidité et communication de crise.34
Lab "Audit Croisé" : Audit complet du projet Capstone d'un pair, aboutissant à un rapport PDF formel qui conditionne la validation du module.
Module 3.3 : Capstone Projects - Le Studio (S41-S48)
La phase finale de production.
Projets Signatures : Développement d'un protocole complexe (DEX, Lending, Infrastructure DePIN) prêt pour le Mainnet.
Critères "Studio-Grade" : Les projets doivent inclure une documentation exhaustive, une couverture de tests >90%, des audits de sécurité internes, et des pipelines CI/CD automatisés. Les builds doivent être vérifiables (Verifiable Builds).35
3. Inventaire Exhaustif des Ressources et de l'Outillage
Cette section fournit la liste précise des outils et configurations nécessaires pour équiper le "Cockpit de l'Architecte" (Annexe F) et définir la "Stack Technique" (Annexe N).
3.1 Environnement de Développement (Le Cockpit Cyborg)
Ces outils constituent l'environnement de travail quotidien de l'étudiant.

Catégorie
Outil / Logiciel
Version Recommandée (2025)
Usage & Justification
OS
Ubuntu Linux
24.04 LTS
Système d'exploitation standard pour les nœuds et le développement Solana.36
Langage
Rust
1.79.0+ (Stable)
Langage cœur. Version alignée avec les exigences du compilateur Solana.37
Framework
Anchor
0.30.1+ (Dernière Stable)
Framework de développement incontournable pour la sécurité et la productivité.12
CLI
Solana CLI
2.0.0+ (Agave)
Interaction avec la blockchain, gestion des clés, déploiement.38
IDE
Cursor / VS Code
Latest
Éditeur de code. Cursor est privilégié pour l'intégration native de l'IA (Cyborg workflow).
Ext. IDE
rust-analyzer
Latest
Support linguistique Rust essentiel pour l'autocomplétion et la détection d'erreurs.
Test
Bankrun
Latest
Framework de test léger et ultra-rapide, remplaçant solana-test-validator pour les tests unitaires.39
Fuzzing
Trident
Latest
Framework de Fuzzing spécifique à Anchor, développé par Ackee.3
Sécurité
Soteria
Latest
Scanner d'analyse statique pour détecter les vulnérabilités courantes (Rust).4
Build
Solana Verify
Latest
Outil pour assurer que le bytecode on-chain correspond au code source (Verifiable Builds).35
Frontend
Solana Web3.js
2.0+
Nouvelle version de la bibliothèque client JavaScript/TypeScript pour les dApps.

3.2 Infrastructure Validator & DevOps (Track N3)
Matériel et logiciel pour le module Validator Architect.

Catégorie
Ressource
Spécifications / Version
Rôle & Détails
Serveur (Mainnet)
Bare Metal
CPU: AMD EPYC 9355 (24c/48t, >3.5GHz)
Le CPU haute fréquence est critique pour le Proof of History. Pas de Xeon basique.5
Mémoire
RAM ECC
256GB (Min) - 512GB (Recommandé)
La RAM ECC est obligatoire pour éviter la corruption de données du Ledger.5
Stockage
NVMe SSD
2x 2TB (Gen4/Gen5) en RAID 1
E/S intensives. Séparation des disques Accounts et Ledger recommandée.26
Réseau
Connexion
1 Gbps Symétrique (Min), 10 Gbps (Rec)
Bande passante massive requise pour la propagation des blocs (Gossip).42
Client 1
Agave
v2.0+
Client de consensus standard (fork de Solana Labs).
Client 2
Jito-Solana
Latest Stable
Client modifié pour capturer la MEV (Maximal Extractable Value).30
Client 3
Firedancer
v0.1+ (Testnet/Frankendancer)
Client haute performance en C++, crucial pour l'avenir du réseau (2025+).28
Monitoring
Stack TIG
Telegraf, InfluxDB, Grafana
Collecte et visualisation des métriques (CPU, RAM, Skip Rate).31
Alerting
PagerDuty
Intégration API
Alertes d'astreinte en cas de délinquance du validateur.

4. Contenus Pédagogiques et Livrables de Production
Pour produire les ressources nécessaires, l'équipe pédagogique doit créer les éléments suivants, basés sur les standards identifiés.
4.1 Les "Golden Standard Repos" (Modèles de Référence)
Il faut produire des dépôts GitHub modèles que les étudiants cloneront ou utiliseront comme référence.
rbk-rust-primitives : Exemples isolés de gestion de mémoire, sérialisation Borsh manuelle, et structures de données Rust sans framework.43
rbk-anchor-scaffold : Un squelette de projet Anchor configuré avec les meilleures pratiques : structure de dossiers modulaire, tests Bankrun pré-configurés, CI/CD GitHub Actions pour le linting et le test.44
rbk-token2022-showcase : Implémentations de référence pour les Transfer Hooks, les frais de transfert et les jetons confidentiels.18
rbk-security-ctf : Une suite de contrats vulnérables (re-entrancy, missing signer, overflow) avec des tests exploitants pour les exercices de "War Room".
4.2 Le "Validator Runbook" (Manuel d'Opérations)
Un document technique exhaustif (Markdown/PDF) pour le Track N3 :
Chapitre 1 : Provisioning. Guide d'installation d'Ubuntu, partitionnement des disques NVMe, configuration du RAID et tuning du kernel Linux (sysctl) pour le réseau haute performance.
Chapitre 2 : Sécurité des Clés. Procédure de génération des clés sur machine "Air-Gapped" (hors ligne). Utilisation de portefeuilles papier et Ledger Nano X pour les clés de retrait.46
Chapitre 3 : Installation des Clients. Scripts d'installation pour Agave et Jito. Configuration des services Systemd.
Chapitre 4 : Monitoring. Modèles JSON pour importer les tableaux de bord Grafana spécifiques à Solana (visualisation des votes, latence, pairs).48
Chapitre 5 : Procédures d'Urgence. Checklists pour le redémarrage de cluster, la gestion de la corruption de ledger, et la rotation des clés en cas de compromission.
4.3 La Grille d'Audit "Guardian" (Checklist)
Un outil pour les revues de code (Skill Mirror) et les audits finaux :
Tableau des Risques : Liste des 20 vulnérabilités les plus courantes sur Solana (ex: "Arbitrary CPI", "Account Data Matching", "Type Cosplay").49
Protocole de Vérification : Étapes pour vérifier formellement chaque instruction : "Est-ce que tous les comptes Signer sont vérifiés?", "Est-ce que les seeds des PDA sont validés?".
Score de Sévérité : Matrice pour classer les bugs trouvés (Critique = Perte de fonds, Haut = Déni de service, etc.) [Annexe E].
5. Gouvernance et Fonctionnement Opérationnel
Le fonctionnement du RBK 2.0 repose sur une gouvernance qui mime celle d'une DAO technique et d'une entreprise d'audit.
5.1 Le Système "Skill Mirror" (Revue par les Pairs)
Inspiré de l'École 42 mais adapté aux enjeux de sécurité critique du Web3.
Fonctionnement : Chaque vendredi, les étudiants soumettent leur code. Ils doivent ensuite auditer le code de deux pairs en utilisant la Grille d'Audit Guardian.
La "Sanction Guardian" : Si une vulnérabilité critique (ex: manque de contrôle d'accès sur une instruction de retrait) est manquée par l'étudiant et par ses auditeurs, le sprint est invalidé pour tous. Cela force une responsabilité collective et une vigilance extrême.1
5.2 Les "Incident Drills" (Simulations de Crise)
Concept : Simuler des conditions de mainnet hostiles.
Scénario : Le "SecLead" (Lead Sécurité) annonce un hack simulé sur les contrats des étudiants déployés sur Testnet.
Action : Les étudiants doivent réagir en temps réel : identifier la faille, utiliser une fonctionnalité de "Circuit Breaker" (pause) si elle a été implémentée, et proposer un patch.
Post-Mortem : L'exercice se conclut par la rédaction d'un rapport Post-Mortem public, pratique standard dans l'industrie.1
5.3 Intégration Écosystémique (Superteam & Bounties)
Pour valider les compétences dans le monde réel, le cursus intègre les opportunités de la Superteam.
Bounties Rémunérés : Les projets de fin de module (N2) sont souvent alignés sur des "Bounties" réels ou des Hackathons en cours. Cela permet aux étudiants de gagner leurs premiers revenus (Earn) tout en apprenant.1
Validator Economy : Les étudiants du Track N3 gèrent l'infrastructure (RPCs) utilisée par les étudiants N1/N2. Si les validateurs tombent, les développeurs ne peuvent plus travailler. Cette interdépendance crée une pression de qualité réaliste (SLA).
6. Recommandations Finales pour la Production des Ressources
Pour lancer ce programme avec le niveau de qualité requis :
Priorité Absolue : Développer le module "Rust for Solana" (N1) avec une emphase sur la gestion mémoire manuelle. C'est le filtre de qualité qui garantira que seuls les profils aptes accèdent au niveau Ingénieur.
Infrastructure : Acquérir ou louer (via des fournisseurs Bare Metal comme Latitude ou Hivelocity) au moins 3 serveurs aux spécifications "Mainnet" pour créer un cluster de test interne réaliste.42
Partenariats : Formaliser les relations avec Jito Labs (pour le curriculum MEV) et Helius (pour l'accès RPC de secours et les webhooks), et s'appuyer sur la Superteam pour le flux de Bounties.1
Formation des Mentors : Les formateurs doivent être certifiés sur la stack 2025 (Anchor 0.30+, Token-2022). Une mise à niveau technique est impérative avant le lancement de la première cohorte.
Ce rapport fournit la structure granulaire, les listes techniques et la philosophie opérationnelle nécessaires pour transformer la vision RBK 2.0 en une réalité pédagogique de classe mondiale.
Sources des citations
Livre_blanc_v5_landscape.pdf
Web3 Developer Tools: Essential Stack for 2025 - Metana, consulté le janvier 6, 2026, https://metana.io/blog/web3-developer-tools-essential-stack-for-2025/
Trident, the first fuzzing framework for Solana programs written in Rust, consulté le janvier 6, 2026, https://usetrident.xyz/
Soteria Audit Action - Marketplace - GitHub, consulté le janvier 6, 2026, https://github.com/marketplace/actions/soteria-audit-action
Solana Validator Requirements, consulté le janvier 6, 2026, https://docs.solanalabs.com/operations/requirements
Deep Dive of the State of Developer Tooling on Solana (July 2025) | by Shubhendu Kumar, consulté le janvier 6, 2026, https://shubhendukumar125.medium.com/deep-dive-of-the-state-of-developer-tooling-on-solana-july-2025-6dd60a4c7555
Developing Programs in Rust - Solana, consulté le janvier 6, 2026, https://solana.com/docs/programs/rust
goheesheng/Rust-Audit-Roadmap - GitHub, consulté le janvier 6, 2026, https://github.com/goheesheng/Rust-Audit-Roadmap
How to Use Program Derived Addresses in Your Solana Anchor Program - Quicknode, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/anchor/how-to-use-program-derived-addresses
developer-content/content/guides/getstarted/intro-to-native-rust.md at main - GitHub, consulté le janvier 6, 2026, https://github.com/solana-foundation/developer-content/blob/main/content/guides/getstarted/intro-to-native-rust.md?plain=1
An Introduction to Anchor: A Beginner's Guide to Building Solana Programs - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/an-introduction-to-anchor-a-beginners-guide-to-building-solana-programs
What has changed from anchor version 0.30.1 to version 0.31.0? - Solana Stack Exchange, consulté le janvier 6, 2026, https://solana.stackexchange.com/questions/20824/what-has-changed-from-anchor-version-0-30-1-to-version-0-31-0
Cross Program Invocation - Solana, consulté le janvier 6, 2026, https://solana.com/docs/core/cpi
Mastering Cross-Program Invocations in Anchor: A Developer's Guide to Solana's CPI Patterns | by Ancilar | Blockchain Services | Medium, consulté le janvier 6, 2026, https://medium.com/@ancilartech/mastering-cross-program-invocations-in-anchor-a-developers-guide-to-solana-s-cpi-patterns-0f29a5734a3e
Cross Program Invocation - Solana, consulté le janvier 6, 2026, https://solana.com/docs/intro/quick-start/cross-program-invocation
Build an Escrow Program on Solana with Anchor | Full Walkthrough by Mike MacCana, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=x7OoYpoWAVM
kobby-pentangeli/solana-escrow: An escrow program (smart contract) built for the Solana blockchain - GitHub, consulté le janvier 6, 2026, https://github.com/kobby-pentangeli/solana-escrow
developer-content/content/guides/token-extensions/transfer-hook.md at main · solana-foundation/developer-content - GitHub, consulté le janvier 6, 2026, https://github.com/solana-foundation/developer-content/blob/main/content/guides/token-extensions/transfer-hook.md?plain=1
Token Extensions: Transfer Hook - Solana, consulté le janvier 6, 2026, https://solana.com/developers/guides/token-extensions/transfer-hook
How to Create and Use Solana Token Extensions Using Anchor | Quicknode Guides, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/anchor/token-2022
Token Extensions | Solana, consulté le janvier 6, 2026, https://solana.com/solutions/token-extensions
All-in-one Metadata with Token22 [Solana Tutorial] - Oct 21st '23 - YouTube, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=uDVk3mmnUUU
A Hitchhiker's Guide to Solana Program Security - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/a-hitchhikers-guide-to-solana-program-security
10 Shocking Solana Security Blunders You're Probably Making (And How to Fix Them), consulté le janvier 6, 2026, https://medium.com/@ancilartech/10-shocking-solana-security-blunders-youre-probably-making-and-how-to-fix-them-3644939c38c4
Introducing Trident: The First Open-Source Fuzzer for Solana Programs - Ackee Blockchain, consulté le janvier 6, 2026, https://ackee.xyz/blog/introducing-trident-the-first-open-source-fuzzer-for-solana-programs/
How to Host a Solana Validator Node: Hardware & Setup Guide - ServerMania, consulté le janvier 6, 2026, https://www.servermania.com/kb/articles/how-to-host-solana-validator-node
Firedancer is live, but Solana is violating the one safety rule Ethereum treats as non-negotiable - CryptoSlate, consulté le janvier 6, 2026, https://cryptoslate.com/firedancer-is-live-but-solana-is-violating-the-one-safety-rule-ethereum-treats-as-non-negotiable/
Getting Started - Firedancer, consulté le janvier 6, 2026, https://docs.firedancer.io/guide/getting-started.html
Jito Bundles: What They Are and How to Use Them - Quicknode, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/transactions/jito-bundles
How to Set Up a Solana Validator - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/how-to-set-up-a-solana-validator
Solana Monitoring by qskyhigh | Grafana Labs, consulté le janvier 6, 2026, https://grafana.com/grafana/dashboards/22716-solana-monitoring-by-qskyhigh/
stakeconomy/solanamonitoring - GitHub, consulté le janvier 6, 2026, https://github.com/stakeconomy/solanamonitoring
Get started with Grafana and Prometheus | Grafana documentation, consulté le janvier 6, 2026, https://grafana.com/docs/grafana/latest/fundamentals/getting-started/first-dashboards/get-started-grafana-prometheus/
PineAnalytics - The History Of All Solana Security Incidents - Reddit, consulté le janvier 6, 2026, https://www.reddit.com/r/solana/comments/1js671t/pineanalytics_the_history_of_all_solana_security/
Verifying Programs | Solana, consulté le janvier 6, 2026, https://solana.com/docs/programs/verified-builds
Agave Validator Requirements, consulté le janvier 6, 2026, https://docs.anza.xyz/operations/requirements
Anchor Build Error: solana-program requires Rust 1.79.0+ but Solana tools use 1.75.0-dev, consulté le janvier 6, 2026, https://solana.stackexchange.com/questions/19629/anchor-build-error-solana-program-requires-rust-1-79-0-but-solana-tools-use-1
Deploying a Solana Rust Program in 2025: Devnet → Mainnet-Beta in 9 Minutes Flat | by PMartin - Medium, consulté le janvier 6, 2026, https://medium.com/@palmartin99/deploying-a-solana-rust-program-in-2025-devnet-mainnet-beta-in-9-minutes-flat-616913bcdb96
What is Bankrun and How to Use it to Enhance Solana Local Development? - Quicknode, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/tooling/bankrun
Testing Solana Programs with Bankrun [Solana Tutorial] - Aug 2nd '24 - YouTube, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=2DVudyfP5bQ
What is Solana Firedancer [Guide for Solana Validators] - Cherry Servers, consulté le janvier 6, 2026, https://www.cherryservers.com/blog/solana-firedancer
How to Choose a Bare Metal Server for Your Solana Validator: Best Configurations for Minimum Requirements (2025) - Inflect, consulté le janvier 6, 2026, https://platform.inflect.com/blog/how-to-choose-a-bare-metal-server-for-your-solana-validator-best-configurations-for-minimum-requirements-(2025)
A repository of Solana program examples - GitHub, consulté le janvier 6, 2026, https://github.com/solana-developers/program-examples
solana-foundation/anchor: Solana Program Framework - GitHub, consulté le janvier 6, 2026, https://github.com/solana-foundation/anchor
civicteam/token-extensions-transfer-hook: A Civic Pass transfer hook for Solana Token2022 - GitHub, consulté le janvier 6, 2026, https://github.com/civicteam/token-extensions-transfer-hook
How to Secure Your Crypto on Solana | by Cody Pritchard | Medium, consulté le janvier 6, 2026, https://medium.com/@cody.pritchard_51949/how-to-secure-your-crypto-on-solana-2d2d70eb02c9
ice-staking/validator-jumpstart: Solana Validator Guide - GitHub, consulté le janvier 6, 2026, https://github.com/ice-staking/validator-jumpstart
Solana Validator Dashboard | Grafana Labs, consulté le janvier 6, 2026, https://grafana.com/grafana/dashboards/14625-solana-validator/
Solana Smart Contract Audits: Key Benefits & Process Breakdown - Antier Solutions, consulté le janvier 6, 2026, https://www.antiersolutions.com/blogs/solana-smart-contract-audits-key-benefits-process-breakdown/
Program security in anchor framework, Solana smart contract security. - Syed Ashar Saghir, consulté le janvier 6, 2026, https://syedashar1.medium.com/program-security-in-anchor-framework-solana-smart-contract-security-b619e1e4d939

