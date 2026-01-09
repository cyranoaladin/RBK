Rapport d'Analyse Stratégique et Pédagogique : Niveau 2 (N2) "Web3 Engineer" - Spécialisation Track A (Solana)
1. Introduction et Cadrage Stratégique : La Genèse du "Guardian"
1.1 Le Contexte de la Transformation : "Senior-by-Design" dans l'Ère Post-Code
L'industrie du développement logiciel traverse une mutation existentielle sans précédent, catalysée par l'émergence des modèles de langage à grande échelle (LLMs) capables de générer du code syntaxiquement correct à une vitesse surhumaine. Dans ce contexte, la formation RBK 2.0 postule que la valeur de l'ingénieur ne réside plus dans l'acte de codage, devenu une commodité, mais dans la capacité d'architecture, d'audit et de sécurisation de systèmes complexes. C'est la thèse fondamentale du paradigme "Senior-by-Design" : il ne s'agit plus de former des exécutants, mais des architectes de la confiance numérique, ou "Guardians", capables de déployer des protocoles financiers inarrêtables.1
Le Niveau 2 (N2), intitulé "Web3 Engineer", incarne le cœur opérationnel de cette vision. Situé entre la phase d'initiation intensive ("La Forge", Semaines 1-12) et le studio de production autonome (Niveau 3, Semaines 29-48), ce segment de 16 semaines (Semaines 13-28) est conçu comme un creuset de haute technicité. Pour la spécialisation Track A, le choix de l'écosystème Solana n'est pas fortuit ; il répond à une stratégie de différenciation radicale sur le marché de l'emploi mondial, où la demande pour l'expertise Rust/Solana dépasse structurellement l'offre, créant une prime à la compétence significative.1
1.2 L'Arbitrage Technologique : La Stratégie "Solana-first, EVM-competent"
L'analyse comparative des écosystèmes blockchain a conduit à un arbitrage technologique décisif pour le programme RBK 2.0 : adopter une posture "Solana-first, EVM-competent". Ce choix repose sur une lecture prospective des besoins de l'infrastructure Web3 de demain, où la performance, la scalabilité et la composabilité financière priment.1
Alors que l'EVM (Ethereum Virtual Machine) reste le standard historique pour la finance décentralisée (DeFi), son architecture séquentielle et son modèle de gaz montrent des limites pour les applications à haute fréquence (Trading, DePIN, Gaming). À l'inverse, la SVM (Solana Virtual Machine), avec son architecture parallèle "Sealevel" et son modèle de compte sans état (stateless), exige une rigueur de programmation système qui forme des ingénieurs intrinsèquement plus robustes. Apprendre Solana, c'est apprendre à gérer la mémoire, la concurrence et les coûts computationnels au niveau du processeur, des compétences transférables et pérennes qui manquent cruellement aux développeurs formés uniquement sur des langages de haut niveau comme Solidity.2
La spécialisation Track A est donc structurée pour transformer des développeurs généralistes en experts de l'ingénierie système appliquée à la blockchain. Elle ne se contente pas d'enseigner un framework, mais plonge dans les entrailles de la machine virtuelle pour en exploiter toute la puissance.
1.3 Architecture Séquentielle du Cursus N2
Le programme de 16 semaines est divisé en quatre modules progressifs, conçus pour déconstruire puis reconstruire les paradigmes de développement de l'étudiant.
Phase
Semaines
Thématique Centrale
Objectifs Pédagogiques & Compétences Clés
Module 1
S13-S16
Le Modèle Solana & Rust Natif
Compréhension "Bare Metal", gestion mémoire, sérialisation manuelle, modèle de compte. Rejet de l'abstraction.
Module 2
S17-S20
Maîtrise du Framework Anchor
Industrialisation, sécurité déclarative, productivité, tests d'intégration TypeScript.
Module 3
S21-S24
Architectures Avancées
Token Extensions (Token-2022), Compression d'état (cNFT), DePIN, Composabilité complexe (CPI).
Module 4
S25-S28
Sécurité & Hardening
Audit, Fuzzing (Trident), Analyse statique (Soteria), préparation au déploiement Mainnet.

Chaque module s'appuie sur la méthodologie "Cyborg 2.0", intégrant l'usage assisté de l'IA pour l'accélération de l'apprentissage (génération de tests, explication de concepts) tout en interdisant formellement la génération de code critique sans audit humain rigoureux ("Don't Trust, Verify").1
2. Module 1 : Fondations Bas Niveau et Rust Natif (Semaines 13-16)
2.1 La Philosophie de "L'Excellence par Rust"
Le premier contact avec le développement Solana dans le Track A est délibérément ardu. Contrairement aux bootcamps qui introduisent immédiatement des frameworks simplificateurs comme Anchor, RBK 2.0 impose une immersion initiale dans le développement "Natif" (Native Rust). Cette approche pédagogique, qualifiée de "Hard Way", est essentielle pour forger des ingénieurs capables de comprendre ce qui se passe "sous le capot". Un architecte qui ne comprend pas la désérialisation binaire ou la gestion des allocations mémoire ne peut pas optimiser un protocole à haute fréquence.4
2.1.1 Consolidation : Ownership, Borrowing et Lifetimes
Les semaines 13 et 14 sont consacrées à l'application stricte des concepts de Rust dans un environnement contraint. La "Piscine Rust" du Niveau 1 a posé les bases ; le Niveau 2 les met à l'épreuve du feu.
Ownership et Déplacement (Move Semantics) : Sur Solana, passer un compte à une fonction n'est pas trivial. Les étudiants doivent maîtriser le transfert de propriété des structures de données. Si une variable est "déplacée" (moved) dans une fonction de traitement, elle n'est plus disponible pour la suite de l'exécution. Cette rigueur prévient les accès concurrents non sécurisés et les fuites de mémoire, des vecteurs d'attaque critiques.6
Emprunt (Borrowing) et Références : La distinction entre référence immuable (&T) et référence mutable (&mut T) est le garde-fou principal du compilateur Rust. Dans le contexte d'un smart contract Solana, où plusieurs instructions peuvent tenter d'accéder au même compte simultanément, le Borrow Checker garantit qu'il n'y a qu'un seul écrivain ou plusieurs lecteurs à un instant T, éliminant de facto les conditions de course (race conditions) au niveau de la compilation.7
Lifetimes (Durées de vie) : Les étudiants apprennent à annoter explicitement les durées de vie ('a, 'info) pour lier la validité des données référencées à la durée de vie de la transaction. C'est particulièrement crucial lors de la manipulation de tranches (slices) de données brutes issues des comptes Solana (AccountInfo), où une mauvaise gestion peut conduire à des références pendantes (dangling pointers).9
2.1.2 Le Modèle de Compte (The Account Model) : Une Rupture Paradigmatique
L'obstacle conceptuel majeur pour les développeurs venant d'Ethereum ou du Web2 est le modèle de compte de Solana.
Architecture Sans État (Stateless) : Contrairement à un contrat Solidity qui encapsule son état (variables de stockage), un programme Solana est purement logique. Il est immuable et sans état. Pour fonctionner, il doit recevoir les données (Comptes) depuis l'extérieur via la transaction. Cette séparation radicale entre le Code (Programme) et la Donnée (Comptes) permet à Solana de paralléliser les transactions qui ne touchent pas aux mêmes données, offrant une scalabilité horizontale massive.10
Anatomie d'un Compte : Les étudiants dissèquent la structure AccountInfo :
key: L'adresse publique du compte.
lamports: Le solde en SOL (pour payer le stockage/rente).
data: Un tableau d'octets (&[u8]) où réside l'état applicatif.
owner: Le programme qui a le droit exclusif de modifier les données (le concept de Program Ownership).
executable: Un flag indiquant si le compte contient du bytecode BPF exécutable.
Cette compréhension granulaire est indispensable pour concevoir des systèmes sécurisés où seul le propriétaire légitime peut muter l'état.12
2.2 Développement en Rust Natif : L'Approche Sans Filet
Durant les semaines 15 et 16, les étudiants construisent leurs premiers programmes en utilisant uniquement la crate solana_program. C'est l'étape où ils apprennent à tout faire manuellement, une compétence qui deviendra leur super-pouvoir lors du débogage de programmes Anchor complexes.
2.2.1 Le Point d'Entrée Unique (Entrypoint)
Tout programme natif commence par une macro entrypoint!. Les étudiants doivent implémenter la fonction process_instruction brute :

Rust


pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult


Ils doivent écrire manuellement le code pour :
Désérialiser les données d'instruction pour savoir quelle fonction appeler (le "dispatch").
Itérer sur le tableau accounts pour extraire les comptes nécessaires.
Vérifier manuellement toutes les contraintes de sécurité : Est-ce que le compte est signé (is_signer)? Est-il accessible en écriture (is_writable)? Est-il possédé par le bon programme (owner)? L'oubli d'une seule de ces vérifications est fatal, et c'est par l'erreur qu'ils apprennent la vigilance.5
2.2.2 La Sérialisation Borsh : Byte par Byte
La communication entre le client (JavaScript/TypeScript) et la blockchain se fait via des tableaux d'octets. RBK impose l'utilisation de Borsh (Binary Object Representation Serializer for Hashing) pour sa compacité et son déterminisme.
Déterminisme et Consensus : Les étudiants apprennent pourquoi l'ordre des champs et la manière dont ils sont sérialisés doivent être strictement identiques sur tous les nœuds du réseau. Une variation infime briserait le consensus.
Implémentation Manuelle : Ils implémentent les traits BorshSerialize et BorshDeserialize sur leurs propres structures Rust, comprenant ainsi le coût en octets de chaque type de donnée (u64 vs u8 vs String). Cette conscience de l'empreinte mémoire est vitale pour l'optimisation des coûts de stockage (Rente).16
2.2.3 Économie du Stockage : Rente et Redimensionnement
Sur Solana, le stockage n'est pas gratuit ; il coûte des SOL sous forme de "Rente" (Rent).
Rent Exemption : Les étudiants calculent le seuil d'exemption de rente. Un compte doit détenir suffisamment de SOL pour couvrir 2 ans de stockage afin de devenir "Rent Exempt" et ne pas être supprimé par le validateur. Ils apprennent à utiliser les syscalls Rent::get() pour calculer dynamiquement ces coûts lors de l'initialisation des comptes.19
Redimensionnement Dynamique (realloc) : Une compétence avancée enseignée est l'utilisation de realloc pour changer la taille d'un compte après sa création (par exemple, pour ajouter des données à un profil utilisateur). Cela implique de gérer minutieusement les frais de rente supplémentaires ou le remboursement en cas de réduction, tout en prévenant les attaques de re-initialisation.22
2.3 Livrables du Module 1
Projet "Native Escrow" : Un contrat d'entiercement (escrow) écrit sans framework, gérant le dépôt et le retrait de fonds entre deux parties.
Audit de Sécurité Interne : Un rapport détaillant comment le code natif gère explicitement les vérifications de signataire et de propriétaire, prouvant que l'étudiant a intériorisé les mécanismes de sécurité de base.1
3. Module 2 : Industrialisation et Maîtrise du Framework Anchor (Semaines 17-20)
3.1 Le Saut vers Anchor : Sécurité et Productivité
Si le Rust natif est l'école de la rigueur, Anchor est l'outil de la production. À partir de la semaine 17, les étudiants basculent vers ce framework qui est à Solana ce que Ruby on Rails est au web : un accélérateur de productivité standardisé. L'objectif n'est pas de masquer la complexité, mais de déléguer la sécurité répétitive à des macros auditées.24
3.2 La Puissance des Macros et la Sécurité Déclarative
Anchor révolutionne le développement Solana en remplaçant des centaines de lignes de code de vérification ("boilerplate") par des annotations déclaratives.
La Macro #[account] : Elle génère automatiquement les implémentations de sérialisation et, surtout, injecte un "discriminateur" unique (hash du nom de la structure) dans les 8 premiers octets du compte. Les étudiants apprennent comment cela prévient les attaques de substitution de compte, où un attaquant essaierait de faire passer un compte de données "Utilisateur" pour un compte "Admin".26
Validation via #[derive(Accounts)] : C'est le cœur du système de sécurité d'Anchor. Les étudiants apprennent à exprimer des contraintes de sécurité complexes directement dans la définition de la structure de données :
#[account(mut)] : Vérifie la mutabilité.
#[account(signer)] : Vérifie la signature.
#[account(has_one = authority)] : Vérifie que le champ authority du compte correspond bien à l'adresse du signataire, verrouillant ainsi l'accès aux seules personnes autorisées.24
#[account(init, payer = user, space = 8 + 64)] : Automatise la création de compte, le calcul de la rente et l'allocation d'espace, éliminant les erreurs manuelles de calcul de lamports vues au Module 1.
3.3 Adresses Dérivées de Programme (PDAs) : L'Identité On-Chain
Les PDAs sont sans doute le concept le plus puissant et le plus difficile de Solana. Ce sont des adresses qui n'ont pas de clé privée, mais qui peuvent être contrôlées programmatiquement par le smart contract.
Conception de Seeds (Graines) : Les étudiants apprennent à concevoir des schémas de dérivation de PDAs robustes et déterministes. Par exemple, pour un compte de profil utilisateur, les seeds pourraient être [b"user_profile", user_pubkey.as_ref()]. Cela garantit qu'il ne peut exister qu'un seul profil par utilisateur, trouvable sans indexeur externe.28
Gestion des Bumps : Ils maîtrisent la notion de "Canonical Bump" (le premier octet qui sort l'adresse de la courbe elliptique) pour sécuriser la dérivation et empêcher des attaquants de créer des PDAs valides mais non contrôlés par le programme.28
Signature Programmatique : Le cas d'usage ultime : le programme utilise le PDA pour signer une transaction en son propre nom (ex: transférer des fonds depuis un coffre-fort). C'est la base de toute application DeFi autonome.30
3.4 Composabilité et Appels Croisés (CPI)
Le Web3 repose sur la capacité des programmes à interagir (Lego Money). Anchor simplifie les Cross-Program Invocations (CPI).
CpiContext : Les étudiants utilisent CpiContext pour empaqueter les comptes et les graines nécessaires à l'appel d'un autre programme (comme le Token Program de Solana).
Interaction avec SPL Token : Un exercice clé est la construction d'un programme qui minte, brûle ou transfère des jetons SPL via CPI. Cela nécessite de comprendre comment passer les "signer seeds" pour que le PDA du programme puisse autoriser le mouvement des fonds.31
Risques d'Arbitrary CPI : Une attention particulière est portée à la validation du program_id cible lors d'un CPI. Les étudiants apprennent à se protéger contre les attaques où un utilisateur malveillant injecterait un faux programme de token pour voler des fonds.33
3.5 L'IDL (Interface Definition Language) et le Frontend
Anchor génère automatiquement un fichier IDL (JSON) qui décrit l'interface du programme.
Typage Fort Côté Client : Les étudiants découvrent comment cet IDL permet de générer des clients TypeScript fortement typés, garantissant que le frontend ne peut pas envoyer de données mal formées au smart contract.
Intégration React/Next.js : Le module se conclut par la connexion du smart contract à une interface utilisateur simple, utilisant wallet-adapter pour la gestion des signatures.34
3.6 Testing Avancé : La Rigueur Industrielle
Le niveau "Senior" se mesure à la qualité des tests.
Tests d'Intégration TypeScript : Utilisation de Mocha et Chai pour simuler des scénarios utilisateurs complets (ex: Alice dépose, Bob retire, Charlie échoue à voler).
Bankrun : Introduction à des outils de test modernes comme solana-bankrun, qui permettent d'exécuter des tests ultra-rapides en manipulant directement l'état de la banque Solana en mémoire, sans lancer un validateur local complet. Cela permet de tester des états impossibles (comme voyager dans le temps pour tester des timelocks).36
4. Module 3 : Architectures Avancées et Innovation (Semaines 21-24)
Ce module propulse les étudiants à la frontière de l'innovation sur Solana, abordant des technologies qui définissent les standards de 2025.
4.1 Token Extensions (Token-2022) : La Nouvelle Norme
Le standard SPL Token historique est remplacé par Token-2022, qui introduit une programmabilité native au niveau du token.38
Transfer Hooks : Les étudiants implémentent des tokens qui exécutent du code à chaque transfert. C'est crucial pour la conformité (RWA) : un token peut vérifier automatiquement si le destinataire est sur une liste blanche (KYC) avant d'accepter la transaction, ou prélever une taxe (royalty) automatiquement.38
Metadata Pointer : Ils apprennent à stocker les métadonnées (nom, image) directement sur le compte du Mint ou via un pointeur flexible, éliminant la dépendance complexe aux programmes de métadonnées tiers.41
Confidential Transfers : Introduction aux transferts confidentiels utilisant des preuves Zero-Knowledge pour masquer les montants, une fonctionnalité clé pour l'adoption institutionnelle et les paiements salariaux sur la blockchain.
4.2 Compression d'État (State Compression) et cNFTs
Pour répondre aux besoins de scalabilité massive (Gaming, DePIN, billetterie), Solana a introduit la compression d'état.
Arbres de Merkle Concurrents : Les étudiants plongent dans la structure de données des "Concurrent Merkle Trees". Au lieu de stocker chaque NFT dans un compte séparé (coûteux en rente), des millions de NFTs sont compressés en une seule empreinte (root hash) stockée on-chain.
Économie d'Échelle : Ils analysent comment cette technologie réduit le coût de minting de 1 million de NFTs de plusieurs centaines de milliers de dollars à quelques centaines.42
Interactions via RPC : Contrairement aux comptes classiques, les données compressées ne sont pas directement lisibles dans l'état global. Les étudiants apprennent à utiliser des indexeurs spécialisés (Read API) et des preuves de Merkle pour interagir avec ces actifs.44
4.3 Optimisation des Compute Units (CU)
Sur une blockchain partagée, l'efficacité est une vertu et une nécessité économique.
Le Budget de Calcul : Chaque transaction a un budget limité de Compute Units (CU). Les étudiants apprennent à profiler leur code pour identifier les fonctions gourmandes.
Techniques d'Optimisation :
Sérialisation Zero-Copy : Utilisation de bytemuck et ZeroCopy pour lire et écrire dans des comptes sans les copier coûteusement dans la mémoire (heap), essentiel pour les jeux ou les carnets d'ordres à haute fréquence.45
Bitwise Operations : Privilégier les opérations bit à bit et les structures de données compactes pour minimiser la consommation CPU.46
5. Module 4 : Sécurité Offensive, Audit et Hardening (Semaines 25-28)
Ce dernier module avant le "Studio de Production" (N3) transforme le développeur en auditeur. La sécurité n'est pas une fonctionnalité, c'est une exigence vitale.
5.1 La Mentalité "Attacker-Controlled"
Les étudiants doivent intégrer que sur Solana, toutes les entrées sont potentiellement malveillantes. Le programme ne doit faire confiance à aucun compte passé en paramètre sans vérification explicite.47
Checklist du Guardian : Ils apprennent à appliquer systématiquement la checklist d'audit :
Est-ce que account_info.owner == expected_program_id? (Ownership Check).48
Est-ce que account_info.is_signer == true pour les opérations sensibles? (Signer Check).
Est-ce que les données du compte ont été initialisées? (Initialization Check).
5.2 Outils d'Audit Avancés : Trident et Soteria
L'audit manuel est complété par des outils automatisés de pointe.
Analyse Statique (Soteria) : Utilisation de scanners comme Soteria pour détecter automatiquement les vulnérabilités de code connues (ex: manque de vérification is_signer) avant même l'exécution.49
Fuzzing (Trident) : Introduction au Fuzzing avec le framework Trident. Les étudiants écrivent des tests qui bombardent le programme avec des millions d'entrées aléatoires et invalides pour tenter de provoquer des états incohérents ou des plantages. C'est la méthode ultime pour découvrir des "edge cases" (cas limites) invisibles à l'œil humain, comme des débordements mathématiques complexes ou des séquences d'instructions inattendues.51
5.3 Infrastructure et Validator Track
Bien que le focus soit le développement, une sensibilisation à l'infrastructure valideur est incluse, préparant le terrain pour ceux qui s'orienteront vers le "Validator Track" ou le module DePIN.
MEV (Maximal Extractable Value) : Comprendre comment les validateurs (via le client Jito) ordonnent les transactions pour extraire de la valeur (arbitrage, sandwiching). Les étudiants apprennent à protéger leurs utilisateurs contre ces attaques (slippage protection) et à utiliser les Jito Bundles pour garantir l'atomicité de leurs propres transactions critiques.54
Performance Réseau : Comprendre l'impact de la géographie des nœuds et de la latence (Gossip protocol) sur la finalité des transactions.1
6. Analyse des Imbrications et Perspectives Professionnelles
6.1 L'Émergence du Profil "Full-Stack Protocol Engineer"
Le programme RBK 2.0 révèle une tendance de fond : la convergence entre le développement de smart contracts et l'ingénierie système. L'architecte Solana de 2025 doit comprendre la gestion bas niveau de la mémoire (comme un développeur C++) tout en maîtrisant les primitives financières de haut niveau (comme un quant). Cette double compétence, forgée par la difficulté de Rust et la puissance d'Anchor, crée un profil "Full-Stack Protocol" capable d'intervenir sur toute la chaîne de valeur, de l'optimisation des opcodes à la stratégie de liquidité DeFi.
6.2 L'Impact des RWA et de la Conformité Programmable
L'insistance du cursus sur Token-2022 (Transfer Hooks) anticipe l'arrivée massive des actifs du monde réel (RWA) sur la blockchain. Les entreprises ne cherchent plus seulement des développeurs capables de lancer un token, mais des ingénieurs capables de coder la régulation au cœur même de l'actif (gel, conformité KYC, taxes). Les diplômés du Track A sont ainsi positionnés non seulement pour le marché crypto-natif, mais aussi pour la transformation numérique des institutions financières traditionnelles.
6.3 Le "Guardian" : Une Réponse à la Crise de Confiance
En intégrant le Fuzzing (Trident) et l'Analyse Statique (Soteria) au cœur du curriculum (et non en option), RBK 2.0 répond à la crise des hacks DeFi. Le "Guardian" n'est pas celui qui développe vite, mais celui qui développe sûr. Cette compétence de "Security-First" est le différenciateur clé qui justifie les niveaux de rémunération élevés et l'attractivité internationale des profils formés.
Synthèse Technique et Outils du Track A
Tableau Comparatif des Paradigmes de Développement
Ce tableau illustre l'évolution des compétences de l'étudiant du Module 1 au Module 2.
Critère
Rust Natif (Semaines 13-16)
Framework Anchor (Semaines 17-20)
Philosophie
"Bare Metal", contrôle total, verbeux.
"Convention over Configuration", sécurisé par défaut.
Gestion des Comptes
Itérateurs manuels, désérialisation explicite.
Injection de dépendances via #[derive(Accounts)].
Sécurité
Vérifications manuelles (if!account.is_signer...).
Contraintes déclaratives (#[account(signer)]).
Productivité
Faible (beaucoup de boilerplate).
Élevée (focus logique métier).
Usage Cible
Optimisation extrême, librairies core, apprentissage.
Applications DeFi, NFT, RWA, Production standard.


Stack Technique et Outillage
1

Domaine
Outils et Technologies Enseignés
Usage Pédagogique et Industriel
Langage Core
Rust (v1.75+)
Gestion mémoire sans GC, typage fort, performance système.
Framework
Anchor (v0.30+)
Développement rapide, génération IDL, sécurité par macros.
Sérialisation
Borsh
Standard binaire compact et déterministe pour les données on-chain.
Sécurité & Audit
Trident (Fuzzing), Soteria (Static Analysis)
Tests de propriétés, détection automatique de failles, audit.
Test & Simulation
Mocha/Chai (TS), Bankrun, LiteSVM
Tests d'intégration complets, simulation d'état rapide (Time travel).
Standards
Token-2022 (Extensions), SPL Token
Standards d'actifs avancés (Hooks, Confidentialité) et classiques.
Compression
Concurrent Merkle Trees, Bubblegum
Gestion d'état à grande échelle (cNFTs) à coût réduit.
Infrastructure
Jito (MEV Bundles), Helius (RPC/DAS)
Optimisation de l'inclusion des transactions et indexation de données.

7. Conclusion
Le Niveau 2 "Web3 Engineer" - Spécialisation Track A de RBK 2.0 est bien plus qu'une formation au code : c'est une école de rigueur industrielle. En forçant les étudiants à traverser la complexité du Rust natif avant de leur donner la puissance d'Anchor, et en les armant des outils de sécurité les plus avancés (Fuzzing, Token-2022), le programme forme une classe d'ingénieurs à part. Ces "Guardians" ne sont pas seulement prêts pour le marché actuel ; ils sont équipés pour construire l'infrastructure financière souveraine et scalable de la prochaine décennie. Ils incarnent la promesse du "Senior-by-Design" : une compétence vérifiable, résiliente et immédiatement déployable sur les défis les plus critiques du Web3.
Sources des citations
Livre_blanc_v5_landscape.pdf
The Solana Architecture: A Comprehensive Deep Dive into the World's Fastest Blockchain | by EuroJohnson | Medium, consulté le janvier 6, 2026, https://medium.com/@neocryptoquant/the-solana-architecture-a-comprehensive-deep-dive-into-the-worlds-fastest-blockchain-12ae70331ab5
Solana vs Sui (2025): Architecture, Execution Models & Security Compared - Three Sigma, consulté le janvier 6, 2026, https://threesigma.xyz/blog/ecosystem/sui-vs-solana-guide
Developing Programs in Rust - Solana, consulté le janvier 6, 2026, https://solana.com/docs/programs/rust
Hello World | Solana, consulté le janvier 6, 2026, https://solana.com/id/developers/courses/native-onchain-development/hello-world-program
Rust Ownership, Borrowing & Lifetimes Explained (2025): The Core Concepts | by Ali Aslam, consulté le janvier 6, 2026, https://medium.com/@a1guy/rust-ownership-borrowing-lifetimes-explained-2025-rusts-secret-sauce-b3e98634f19b
Advanced Rust: Understanding Ownership, Borrowing, and Lifetimes - NamasteDev Blogs, consulté le janvier 6, 2026, https://namastedev.com/blog/advanced-rust-understanding-ownership-borrowing-and-lifetimes/
For Beginners: An interesting article about Ownership and Borrowing - tutorials - The Rust Programming Language Forum, consulté le janvier 6, 2026, https://users.rust-lang.org/t/for-beginners-an-interesting-article-about-ownership-and-borrowing/108718
Mastering Ownership, Moves, Borrowing, and Lifetimes in Rust - DEV Community, consulté le janvier 6, 2026, https://dev.to/amritsingh183/mastering-ownership-moves-borrowing-and-lifetimes-in-rust-5077
What is the Solana Account Model? - Alchemy, consulté le janvier 6, 2026, https://www.alchemy.com/overviews/solana-account-model
The Solana Programming Model: An Introduction to Developing on Solana - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/the-solana-programming-model-an-introduction-to-developing-on-solana
Deep Dive into Solana's Account Model: The Backbone of Solana's Architecture - DEV Community, consulté le janvier 6, 2026, https://dev.to/ayxshsoni/deep-dive-into-solanas-account-model-the-backbone-of-solanas-architecture-22a2
Accounts | Solana, consulté le janvier 6, 2026, https://solana.com/docs/core/accounts
Rust Program Structure | Solana, consulté le janvier 6, 2026, https://solana.com/docs/programs/rust/program-structure
entrypoint in solana_program - Rust - Docs.rs, consulté le janvier 6, 2026, https://docs.rs/solana-program/latest/solana_program/macro.entrypoint.html
Borsh: A Comprehensive Guide and Its Role in Anchor for Solana | by Yong kang Chia, consulté le janvier 6, 2026, https://extremelysunnyyk.medium.com/borsh-and-its-role-in-anchor-for-solana-48c19308328f
Instruction in solana_instruction - Rust - Docs.rs, consulté le janvier 6, 2026, https://docs.rs/solana-instruction/latest/solana_instruction/struct.Instruction.html
Serializing Data - Solana Cookbook, consulté le janvier 6, 2026, https://solanacookbook.com/guides/serialization.html
How to Use getMinimumBalanceForRentExemption - Helius Docs, consulté le janvier 6, 2026, https://www.helius.dev/docs/rpc/guides/getminimumbalanceforrentexemption
Cost of storage, maximum storage size, and account resizing in Solana | By RareSkills, consulté le janvier 6, 2026, https://rareskills.io/post/solana-account-rent
What is Rent on Solana and How to Calculate it | Quicknode Guides, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/getting-started/understanding-rent-on-solana
What's the best approach to extend program owned account to add some new fields?, consulté le janvier 6, 2026, https://solana.stackexchange.com/questions/23172/whats-the-best-approach-to-extend-program-owned-account-to-add-some-new-fields
How to Calculate Space for PDA Accounts with Dynamic Vectors in Solana?, consulté le janvier 6, 2026, https://solana.stackexchange.com/questions/17649/how-to-calculate-space-for-pda-accounts-with-dynamic-vectors-in-solana
An Introduction to Anchor: A Beginner's Guide to Building Solana Programs - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/an-introduction-to-anchor-a-beginners-guide-to-building-solana-programs
Anchor Framework, consulté le janvier 6, 2026, https://www.anchor-lang.com/
Program Structure - Anchor Docs, consulté le janvier 6, 2026, https://www.anchor-lang.com/docs/basics/program-structure
How to Use Account Constraints in Your Solana Anchor Program | Quicknode Guides, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/anchor/how-to-use-constraints-in-anchor
Program-Derived Address - Solana, consulté le janvier 6, 2026, https://solana.com/docs/core/pda
Program Derived Address - Anchor Docs, consulté le janvier 6, 2026, https://www.anchor-lang.com/docs/basics/pda
Solana Explained: Accounts, PDAs, CPIs & Anchor CRUD Demo - YouTube, consulté le janvier 6, 2026, https://www.youtube.com/watch?v=QtHVPdygNuQ
What is a Cross Program Invocation (CPI) on Solana? | Quicknode Guides, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/anchor/what-are-cpis
cpi - Cross Program Invocation - Anchor Docs, consulté le janvier 6, 2026, https://www.anchor-lang.com/docs/basics/cpi
slowmist/solana-smart-contract-security-best-practices - GitHub, consulté le janvier 6, 2026, https://github.com/slowmist/solana-smart-contract-security-best-practices
How to Connect a Wallet with React - Solana, consulté le janvier 6, 2026, https://solana.com/developers/cookbook/wallets/connect-wallet-react
How to Connect Users to Your dApp with the Solana Wallet Adapter and Scaffold, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/dapps/how-to-connect-users-to-your-dapp-with-the-solana-wallet-adapter-and-scaffold
Professional workflow for Anchor Tests - Solana Stack Exchange, consulté le janvier 6, 2026, https://solana.stackexchange.com/questions/21115/professional-workflow-for-anchor-tests
running tests with bankrun and jest on solana | by deauth - Medium, consulté le janvier 6, 2026, https://medium.com/@anurage66/running-tests-with-bankrun-and-jest-on-solana-9e28c0a9b1d6
Token Extensions: Transfer Hook - Solana, consulté le janvier 6, 2026, https://solana.com/developers/guides/token-extensions/transfer-hook
What are Solana SPL Token Extensions and How to Get Started? | Quicknode Guides, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/spl-tokens/token-2022/overview
What is the Solana Transfer Hook Extension | Quicknode Guides, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/spl-tokens/token-2022/transfer-hooks
Metadata & Metadata Pointer Extensions - Solana, consulté le janvier 6, 2026, https://solana.com/docs/tokens/extensions/metadata
Account Compression Proof Changes - Solana Stack Exchange, consulté le janvier 6, 2026, https://solana.stackexchange.com/questions/9548/account-compression-proof-changes
How to use compressed NFTs on Solana, powered by state compression, consulté le janvier 6, 2026, https://solana.com/news/how-to-use-compressed-nfts-on-solana
What are Compressed NFTs and How to Mint one on Solana | Quicknode Guides, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/nfts/mint-compressed-nft
Optimizing Solana Programs - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/optimizing-solana-programs
Ultimate Solana Optimization Guide 2024: Boost Performance & Efficiency, consulté le janvier 6, 2026, https://www.rapidinnovation.io/post/solana-optimization-and-best-practices-guide
A Hitchhiker's Guide to Solana Program Security - Helius, consulté le janvier 6, 2026, https://www.helius.dev/blog/a-hitchhikers-guide-to-solana-program-security
Solana Security Risks, Issues & Mitigation Guide - Cantina.xyz, consulté le janvier 6, 2026, https://cantina.xyz/blog/securing-solana-a-developers-guide
10 Shocking Solana Security Blunders You're Probably Making (And How to Fix Them), consulté le janvier 6, 2026, https://medium.com/@ancilartech/10-shocking-solana-security-blunders-youre-probably-making-and-how-to-fix-them-3644939c38c4
silas-x/soteria-action: GitHub Action for Soteria, consulté le janvier 6, 2026, https://github.com/silas-x/soteria-action
Trident, the first fuzzing framework for Solana programs written in Rust, consulté le janvier 6, 2026, https://usetrident.xyz/
Trident Brings Manually Guided Fuzzing to Solana - Ackee Blockchain, consulté le janvier 6, 2026, https://ackee.xyz/blog/trident-brings-manually-guided-fuzzing-to-solana/
README.md - Ackee-Blockchain/Solana-Auditors-Bootcamp - GitHub, consulté le janvier 6, 2026, https://github.com/Ackee-Blockchain/Solana-Auditors-Bootcamp/blob/master/Lesson-3/README.md
Jito Bundles: What They Are and How to Use Them - Quicknode, consulté le janvier 6, 2026, https://www.quicknode.com/guides/solana-development/transactions/jito-bundles
Jito Solana MEV Bot Development: A Comprehensive Guide - Calibraint, consulté le janvier 6, 2026, https://www.calibraint.com/blog/everything-about-jito-solana-mev-bot-development

