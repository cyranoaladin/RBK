Addendum Technique RBK 3.0 : Infrastructure de Sécurisation Financière Trustless
1. Introduction Stratégique : Du Contrat Social au Code Immuable
L'évolution des modèles de financement de l'éducation, en particulier les Accords de Partage de Revenus (Income Share Agreements - ISA), se heurte historiquement à un obstacle majeur : le "Trust Gap" ou fossé de confiance. Les modèles traditionnels d'ISA reposent sur des promesses juridiques, des systèmes de recouvrement de créances coûteux et une réconciliation manuelle des revenus, processus intrinsèquement frictionnels, juridiquement onéreux et souvent adversariaux. Le présent addendum au Livre Blanc RBK 3.0 propose un changement de paradigme fondamental : la transition de l'ISA en tant que promesse légale vers l'ISA en tant qu'instrument financier programmable.
En exploitant la composabilité de la Machine Virtuelle Ethereum (EVM) et des solutions de mise à l'échelle de couche 2 (telles que Base, Polygon ou Gnosis Chain), nous définissons ici une infrastructure "Risk-Free". Ce système ne repose pas sur la bonne volonté de l'apprenant, mais sur des garanties cryptographiques. L'architecture intègre Safe pour l'abstraction de compte, 0xSplits pour le routage des revenus, ERC-3525 pour la tokenisation de la dette, Monerium pour le pontage fiat-on-chain, Sablier pour le streaming de paiement et Kleros pour l'arbitrage décentralisé.
L'objectif est de créer une "Banque Autonome" pour chaque apprenant, où l'alignement des intérêts (partage 90/10 pendant la formation et remboursement de 15% post-formation) est exécuté par une logique de contrat intelligent immuable plutôt que par une intervention humaine. Ce document fournit une spécification technique exhaustive, une analyse des risques et un guide de mise en œuvre pour cet écosystème, enrichissant la proposition initiale avec les outils les plus robustes disponibles en 2025.
2. Protocole "In-Share" 90/10 : Architecture du Portefeuille Souverain et Capture de Valeur
La phase de formation chez RBK est caractérisée par une génération de valeur immédiate via des Bounties, Grants et Hackathons. La proposition initiale suggère un partage 90/10. Pour rendre ce partage "trustless" (sans nécessité de confiance), il est impératif de dépasser le simple portefeuille EOA (Externally Owned Account) pour adopter une architecture de compte intelligent modulaire.
2.1 Architecture du Coffre-Fort Numérique (Safe Smart Account)
La pierre angulaire de l'infrastructure RBK 3.0 est le déploiement d'un Safe (anciennement Gnosis Safe) pour chaque apprenant dès l'onboarding.1 Contrairement à un portefeuille MetaMask classique contrôlé par une clé privée unique (ce qui représente un point de défaillance unique et un risque de sécurité), le Safe est un contrat intelligent programmable qui permet une gestion granulaire des actifs et des permissions.
2.1.1 Configuration Multisignature et Hiérarchie des Clés
Le Safe de l'apprenant est configuré non pas comme un simple stockage, mais comme un véhicule d'investissement conjoint durant la phase de formation. La configuration optimale recommandée est un schéma multisignature 2-sur-3, offrant un équilibre entre souveraineté de l'utilisateur et sécurité du protocole :
Clé A (Apprenant) : Cette clé détient les droits d'initiation des transactions. Elle permet à l'apprenant de proposer des interactions avec des protocoles DeFi, de signer des messages pour l'authentification et de gérer l'aspect opérationnel quotidien.
Clé B (Guardian RBK) : Cette clé, détenue par l'infrastructure RBK (automatisée via un serveur sécurisé ou un autre Safe institutionnel), agit comme co-signataire obligatoire pour les transactions sortantes ne respectant pas les règles préétablies. Elle détient un droit de veto algorithmique.
Clé C (Oracle de Récupération / Escrow) : Une troisième clé est détenue par un module de récupération sociale ou un tiers de confiance décentralisé (ex: un tribunal Kleros ou un service de garde institutionnel). Cette clé n'intervient qu'en cas de perte de clé par l'apprenant ou de litige majeur nécessitant une intervention externe.2
2.1.2 Abstraction de Compte (ERC-4337) et Paymasters
L'expérience utilisateur (UX) est critique pour l'adoption. L'utilisation du standard ERC-4337 permet de transformer le Safe en un "Smart Account" capable de bénéficier des Paymasters.3
Dans le contexte RBK, cela signifie que l'apprenant n'a pas besoin de posséder de l'ETH ou du MATIC pour payer les frais de gaz initiaux. Un contrat Paymaster financé par RBK sponsorise les transactions liées aux opérations éducatives (déploiement de contrats, signature de présences, réception de bourses). Cette abstraction élimine la friction financière à l'entrée et garantit que l'incapacité de payer le gaz ne peut jamais être invoquée comme excuse pour le non-respect des obligations contractuelles.
2.1.3 Modules Zodiac pour la Gouvernance Programmable
Pour appliquer le protocole "In-Share" sans nécessiter une signature manuelle de RBK à chaque micro-transaction, nous intégrons les Modules Zodiac de Gnosis Guild.5 Ces modules étendent les fonctionnalités du Safe en lui permettant d'exécuter des transactions sans signature multisig si elles respectent des conditions strictes.
Implémentation du "Roles Modifier" :
Nous utilisons le module Zodiac Roles Modifier pour accorder à la clé de l'apprenant un rôle spécifique.7 Ce rôle lui permet d'exécuter unilatéralement des transactions si et seulement si :
Destination : Les fonds sont envoyés vers des adresses whitelistées (ex : protocoles d'échange de stablecoins, plateformes de hackathons).
Scope : L'apprenant peut retirer librement les fonds présents dans le "Pocket Wallet" (les 10% qui lui reviennent), mais n'a aucun droit de signature unilatérale sur les fonds destinés au Trésor RBK.
Interdiction de Mixers : Le module interdit explicitement les interactions avec des contrats comme Tornado Cash, assurant la traçabilité des fonds pour des raisons de conformité.8
2.2 Le Moteur de Ventilation : Splitter Contract (0xSplits)
Le cœur du mécanisme de partage 90/10 est le contrat Splitter, basé sur l'architecture 0xSplits v2.9 Ce contrat est déployé de manière déterministe (via CREATE2) pour chaque apprenant, garantissant une adresse de réception immuable et prédictible.
2.2.1 Logique de Ventilation Hard-Codée
Le contrat Splitter est configuré avec deux bénéficiaires immuables :
Trésor RBK : Allocation de 90.00% (soit 900,000 points de base).
Safe de l'Apprenant : Allocation de 10.00% (soit 100,000 points de base).
Contrairement à un simple virement, l'utilisation de 0xSplits permet de gérer une multitude de tokens (ERC-20) et d'ETH natif sans reconfiguration. Tout actif envoyé à l'adresse du Splitter est mathématiquement dû aux bénéficiaires selon les ratios définis. L'immuabilité du contrat garantit à RBK que les règles du jeu ne peuvent être changées unilatéralement par l'apprenant en cours de route.11
2.2.2 Automatisation de la Distribution : Le Modèle "Push"
Par défaut, 0xSplits utilise un modèle "Pull" (les bénéficiaires doivent réclamer leurs fonds). Pour maximiser l'efficacité et réduire la charge cognitive de l'apprenant, nous automatisons ce processus via Gelato Network ou Chainlink Automation.12
Workflow d'Automatisation :
Trigger (Déclencheur) : Un "Web3 Function" de Gelato surveille le solde du contrat Splitter.
Condition : Si le solde dépasse un seuil de rentabilité de gaz (ex: > 10 USDC), le bot active la fonction distribute().
Exécution : La fonction distribute() calcule les parts, transfère 90% au Trésor et 10% au Safe de l'apprenant.
Incentive : Une micro-commission (ex: 0.1%) est prélevée sur le montant distribué pour payer le bot Gelato, rendant le système économiquement autonome et résilient à la censure.14
2.3 Conditionnalité de Graduation et Venture Engine
L'intégration technique avec le Venture Engine (la plateforme pédagogique off-chain) est cruciale. Le Venture Engine agit comme un observateur de la blockchain.
Validation des Bounties : Lorsqu'un apprenant déclare avoir gagné un hackathon, le Venture Engine interroge la blockchain (via un sous-graphe The Graph ou une API RPC) pour vérifier que les fonds ont bien été reçus sur l'adresse du Splitter et non sur une adresse personnelle.
Sanction Automatique : Si les fonds ne sont pas détectés sur le Splitter, le jalon pédagogique associé reste bloqué ("Pending Verification"), empêchant l'accès aux modules suivants. Cela crée une boucle de rétroaction immédiate : pas de partage, pas de progression.
3. Architecture ISA Smart-Contract : Tokenisation de la Dette (Phase Post-Formation)
Une fois la formation terminée, l'obligation de l'apprenant change de nature. Elle passe d'un partage de revenus ponctuels (Bounties) à un engagement de long terme sur le salaire (ISA). Pour gérer cette complexité financière, nous transformons le contrat ISA papier en un actif numérique programmable : le CPPS (Career Path Protection Security).
3.1 Le Standard ERC-3525 : Semi-Fungible Token (SFT)
Pour représenter la dette de l'ISA, les standards classiques ERC-20 (trop fongibles) ou ERC-721 (trop uniques) sont insuffisants. Nous adoptons le standard ERC-3525, développé par Solv Protocol, qui est spécifiquement conçu pour les instruments financiers complexes comme les obligations et les vesting vouchers.15
3.1.1 Pourquoi ERC-3525 est supérieur pour les ISA?
L'ERC-3525 introduit une structure de données à trois niveaux qui modélise parfaitement la dette étudiante :
ID (Identifiant Unique) : Chaque jeton représente un contrat spécifique lié à un étudiant unique. Cela permet de tracer l'historique de remboursement individuel.
Slot (Attribut de Catégorie) : Le "Slot" permet de regrouper les tokens par caractéristiques communes. Pour RBK, un Slot pourrait correspondre à une "Cohorte 2026 - Risque A" ou "Programme Data Science". Cela rend les dettes fongibles au sein d'une même catégorie, facilitant leur regroupement pour des investisseurs potentiels.18
Value (Montant Quantitatif) : Contrairement à un NFT statique, un SFT possède une "valeur" intrinsèque (ex: 15,000 USD de Cap). Cette valeur peut être fractionnée. RBK peut, par exemple, diviser le SFT d'un étudiant en deux : garder 50% de la dette et vendre 50% à un fournisseur de liquidité, tout en conservant la gestion unique du contrat.19
3.1.2 Comparaison Technique : ERC-3525 vs Obligate/ERC-3475
Bien que le protocole Obligate utilise une structure propriétaire inspirée de l'ERC-3475 pour des obligations régulées 20, et que l'ERC-3475 offre des "Abstract Storage Bonds" très flexibles 21, l'ERC-3525 est retenu pour sa rétrocompatibilité avec l'ERC-721.
Cela signifie que le contrat de dette de l'étudiant peut être visualisé directement dans n'importe quel portefeuille compatible NFT (MetaMask, Rainbow) et potentiellement listé sur des places de marché NFT si nécessaire, offrant une transparence et une accessibilité supérieures pour l'utilisateur final.
Caractéristique
ERC-20
ERC-721 (NFT)
ERC-3525 (SFT - Retenu)
ERC-3475
Unicité
Non
Oui
Oui (ID)
Oui
Valeur Quantitative
Oui
Non
Oui (Propriété Value)
Oui
Fractionnement
N/A
Impossible
Natif
Natif
Structure de Données
Aucune
URI Statique
Dynamique / Slot
Hiérarchique Complexe
Compatibilité Wallet
Haute
Haute
Haute (via ERC-721)
Basse (Nécessite UI spécifique)

3.2 Cycle de Vie du Contrat CPPS
Le contrat intelligent CPPS encapsule toute la logique financière de l'ISA :
Initialisation : À la graduation, le Venture Engine déclenche le mint() du SFT. La propriété Value est initialisée au Cap de Remboursement maximum (ex: 15,000 USD). La propriété Maturity est fixée à la durée maximale (ex: 5 ans).
Amortissement Automatique : À chaque fois qu'un paiement est reçu via le flux de streaming (voir Section 5), le contrat appelle une fonction amortize(). Cette fonction réduit la Value du SFT en temps réel.
Clôture (Burn) : Lorsque la Value atteint 0 (dette remboursée) ou que la date Maturity est dépassée, le SFT est automatiquement brûlé (burn()), émettant un événement DebtDischarged qui libère l'apprenant de toute obligation future.
4. Le Pont Fiat-On-Chain et Oracles de Revenus : Détection et Capture
Le point de défaillance critique de la plupart des ISA blockchain est le "problème de l'off-ramp" : les apprenants reçoivent leur salaire en monnaie fiduciaire (TND, EUR, USD) sur des comptes bancaires traditionnels, invisibles pour la blockchain. RBK 3.0 comble cette lacune en utilisant une triade technologique : Monerium, Request Network et Reclaim Protocol.
4.1 La "Banque Auto-Custodiale" : Intégration IBAN Monerium
Pour les apprenants travaillant avec des clients internationaux ou européens, Monerium fournit la solution ultime : des IBANs on-chain.22
Mécanisme : Monerium émet un IBAN dédié au nom de l'apprenant, qui est cryptographiquement lié à son Safe Smart Account.
Le Flux Financier :
L'employeur effectue un virement SEPA en Euros vers cet IBAN Monerium.
Tokenisation Automatique : Dès réception des fonds bancaires, le système Monerium minte automatiquement des tokens EURe (un stablecoin de monnaie électronique régulé) et les envoie sur le Safe de l'apprenant.24
Déclencheur On-Chain : Cette transaction entrante est un événement visible sur la blockchain. Grâce à Chainlink Automation (Log Triggers), la réception des EURe déclenche instantanément la logique de prélèvement ISA.25
Conformité MiCA : L'EURe étant de la monnaie électronique régulée (Electronic Money Token sous MiCA), il offre une sécurité juridique équivalente aux dépôts bancaires, protégeant les fonds de l'apprenant.27
4.2 Facturation Automatisée : Request Network
Pour les freelances ou les contrats B2B, RBK intègre Request Network.29
Smart Invoicing : L'apprenant génère ses factures via un dashboard RBK en marque blanche propulsé par Request.
Logique Embarquée : Le contrat de facturation permet au payeur (employeur) de régler en n'importe quelle devise, mais le règlement final est codé pour transiter par le Splitter de l'apprenant.
Système d'Enregistrement : Request crée une preuve immuable de la facture et de son statut (Payé/Impayé). Cela sert d'oracle de vérité pour le Venture Engine : si une facture est marquée "Payée" sur Request mais que les 15% ne sont pas arrivés à RBK, une alerte de fraude est levée.31
4.3 La Solution "Boîte Noire" : Reclaim Protocol (zkTLS)
Pour les apprenants recevant des salaires en TND sur des banques locales sans interface crypto, nous utilisons Reclaim Protocol (zkTLS) comme mécanisme de vérification de dernier recours.32
Preuves à Divulgation Nulle de Données Web2 : Reclaim permet à l'apprenant de se connecter au site web de sa banque (ex: Biat, Amen Bank) via un proxy client sécurisé. Le protocole génère une Preuve à Divulgation Nulle (Zero-Knowledge Proof - ZKP) qui atteste l'existence d'une transaction (ex: "Virement reçu de Société X > 2,500 TND") sans jamais révéler les identifiants de connexion ni l'historique complet des dépenses.34
Trigger de Sanction : Les apprenants sans revenus on-chain détectés sont tenus de soumettre ces preuves mensuellement. L'absence de preuve (ou une preuve contradictoire) agit comme un oracle pour le protocole de "Slashing".
Préservation de la Vie Privée : Grâce aux zk-SNARKs, RBK ne voit pas le relevé bancaire de l'étudiant. Le contrat intelligent reçoit simplement une valeur booléenne : Revenu_Verifie : VRAI/FAUX.
5. Flux de Remboursement Automatisé : Money Streaming
Une fois le revenu détecté (via Monerium EURe ou dépôt stablecoin vérifié), la logique de remboursement s'active. Nous abandonnons les paiements mensuels manuels pour adopter le Money Streaming en Temps Réel via Sablier V2.
5.1 Sablier V2 et les Flux "Lockup Dynamic"
Nous utilisons les contrats LockupDynamic de Sablier V2 pour créer des flux de paiement flexibles mais garantis.36
Mécanisme Opérationnel :
Interception : Le revenu (ex: 2,000 EURe) arrive sur le Safe.
Calcul : Un module Zodiac configuré avec la logique ISA intercepte les fonds. Il calcule 15% (300 EURe).
Création du Stream : Le module approuve le contrat Sablier et appelle createStream avec les paramètres suivants :
Montant : 300 EURe.
Durée : 30 jours (jusqu'au prochain cycle de paie).
Recipient : Trésor RBK.
Distribution Continue : Les 300 EURe ne sont pas envoyés d'un coup. Ils sont "streamés" seconde par seconde vers RBK.
Avantage Psychologique et Financier :
Cette méthode réduit la "douleur du paiement". L'apprenant voit son revenu disponible (85%) immédiatement, tandis que le service de la dette s'opère en arrière-plan, de manière fluide, mimant le prélèvement à la source des impôts. De plus, cela offre à RBK une trésorerie en temps réel plutôt que par à-coups mensuels.38
5.2 Superfluid pour les Salaires Web3 Natifs
Si l'apprenant travaille pour une DAO Web3 qui utilise déjà le streaming pour la paie (via Superfluid), la logique est encore plus simple. La DAO streame le salaire brut vers un Superfluid Splitter contrôlé par le Safe de l'apprenant. Ce Splitter divise automatiquement le flux à la source : 15% sont redirigés vers RBK, et 85% continuent vers le portefeuille de l'apprenant.39 Cela élimine totalement l'apprenant de la boucle de décision de paiement.
6. Identité et Réputation : Le Soulbound Token (SBT) Révocable
Pour lier le comportement financier à la réputation professionnelle, nous implémentons l'ERC-5192 (Minimal Soulbound NFTs). Ce token représente le diplôme et le statut de l'apprenant au sein du réseau.40
6.1 Gestion Dynamique des États (State Management)
Le SBT n'est pas une image statique. C'est un token dynamique dont les métadonnées et l'état sont pilotés par le contrat ISA.
État 0 (Vert) : "Actif - Good Standing"
Condition : Les paiements sont à jour via Sablier, ou le revenu déclaré est sous le seuil.
Utilité : Donne accès au réseau Alumni RBK, aux protocoles de "Job Gating" et aux pools de prêts préférentiels.
État 1 (Jaune) : "Warning - Vérification Requise"
Condition : Aucun revenu on-chain détecté depuis 60 jours, et aucune preuve Reclaim soumise.
Utilité : Restreint l'accès aux fonctionnalités premium ; envoie des notifications push on-chain (XMTP) au Safe de l'apprenant.
État 2 (Rouge) : "Défaut - Suspendu"
Condition : Défaut confirmé ou fraude avérée (après arbitrage Kleros).
Utilité : Les métadonnées du SBT se mettent à jour pour afficher visuellement "DEFAULTED". Ceci est visible publiquement sur OpenSea, LinkedIn (via plugins de vérification) et tout parseur de CV Web3.
6.2 Mécanisme de "Burn" et "Lock"
L'ERC-5192 inclut une fonction standard locked() qui empêche le transfert.41 Le token est lié à vie au Safe de l'apprenant ; il ne peut pas le déplacer vers un nouveau portefeuille pour cacher son historique.
Cependant, contrairement aux NFTs standards, l'Émetteur (RBK) conserve un privilège de burn ou revoke. En cas de défaut total confirmé, le Multisig RBK (ou le contrat Governor) peut appeler revoke(tokenId), supprimant effectivement le diplôme de la blockchain.40
7. Protocole de Sanction et Slashing de Réputation
RBK 3.0 transforme le défaut de paiement d'un litige civil classique en un Événement de Slashing Réputationnel. Le système utilise le "Capital Social" comme collatéral, remplaçant le collatéral financier absent.
7.1 La Boucle de Surveillance On-Chain
Oracle Watchtower : Un service automatisé (Chainlink Automation ou Gelato) surveille en permanence les contrats Monerium et Splitter.
Détection de Discrépance : Si des données externes (ex: une mise à jour LinkedIn détectée par un oracle de scraping) entrent en conflit avec les données internes (0 revenu on-chain), le Watchtower flag le compte.
Période de Challenge : Le contrat entre en "Mode Challenge" pour 10 jours. L'apprenant est notifié. Il doit soumettre une preuve Reclaim (zkTLS) pour expliquer la divergence (ex: "La mise à jour LinkedIn correspond à un stage non rémunéré").
7.2 L'Exécution des Conséquences
Si l'apprenant ne fournit pas de vérification sous 10 jours :
Étape 1 : Impact Score de Crédit. RBK met à jour le registre de score de crédit on-chain (via des protocoles comme Spectra ou Arcx).43 Cela blacklist effectivment l'apprenant des protocoles de prêt DeFi sous-collatéralisés.
Étape 2 : Slashing du SBT. L'état du SBT passe au Rouge/Défaut.
Étape 3 : Registre Public. L'adresse de l'apprenant est inscrite dans un contrat "Registry of Non-Compliance". Ce registre est consultable par les recruteurs partenaires, créant une désincitation professionnelle massive à la fraude.
8. Arbitrage Décentralisé : Intégration de la Cour Kleros
Pour éviter le risque de centralisation où RBK agirait comme juge et partie, nous intégrons Kleros comme la "Cour Suprême" du protocole.45 Ceci est aligné avec le Standard d'Arbitrage (ERC-792).
8.1 Le Flux de Litige
Escalade : Si un apprenant estime avoir été sanctionné à tort (ex: défaut déclenché alors qu'il était hospitalisé), il peut payer des frais d'arbitrage (en ETH ou PNK) pour escalader le dossier vers Kleros.
Soumission de Preuves (ERC-1497) :
RBK soumet : Les logs de transaction on-chain (ou leur absence), les rapports d'échec zkTLS.
Apprenant soumet : Relevés bancaires off-chain (PDF hashés sur IPFS), certificats médicaux (cryptés).
Le Jury : Kleros sélectionne des jurés aléatoires et anonymes (incités par la théorie des jeux / Point de Schelling) pour examiner le cas.47
Le Verdict : Les jurés votent.
Si l'Apprenant Gagne : Le protocole rétablit automatiquement le SBT au statut "Vert" et rembourse les frais d'escalade.
Si RBK Gagne : Le statut "Rouge" est confirmé définitivement.
8.2 Le Contrat Governor pour l'Exécution Forcée
Pour garantir l'exécution sans intervention humaine, nous utilisons un Kleros Governor Contract. Ce contrat détient les permissions administratives sur les contrats RBK. Il ne peut appeler la fonction revoke() que si un litige a été résolu en faveur de RBK par la cour Kleros. Cela protège l'apprenant contre une censure arbitraire ou une corruption interne chez RBK.46
9. Synthèse des Procédures d'Intégration et Roadmap Technique
Le tableau suivant résume l'intégration technique des modules proposés pour la mise à jour du Livre Blanc :
Phase
Action Technique
Outil / Standard
Déclencheur / Enforceur
Onboarding
Déploiement Wallet Multisig
Safe (ERC-4337)
Nexus (Usine RBK)
Formation
Ventilation Revenus (90/10)
0xSplits + Gelato
Transaction Entrante
Graduation
Mint de la Dette (SFT)
ERC-3525 + ERC-5192
Venture Engine
Emploi
Fiat On-Ramp & Invoicing
Monerium (IBAN) / Request
Virement SEPA
Remboursement
Streaming des 15%
Sablier V2 (Lockup Dynamic)
Module Zodiac
Vérification
Preuve de Revenu Off-chain
Reclaim Protocol (zkTLS)
Oracle / Watchtower
Litige
Arbitrage Décentralisé
Kleros + Reality.eth
Transaction Contestée
Sanction
Révocation & Slashing
Governor Contract
Verdict Kleros

10. Argumentaire pour le CEO : Le Paradigme "Risk-Free"
Cette architecture représente une évolution fondamentale : le passage de l'Application Légale à l'Application Cryptographique.
La Fraude devient Professionnellement Suicidaire : En liant le Diplôme (SBT) à la Dette (ISA), nous créons un système où faire défaut sur sa dette revient à supprimer son propre diplôme. Avec l'intégration des registres de réputation on-chain (Spectra/Arcx), un défaut rend l'apprenant "radioactif" pour les futurs employeurs Web3.
Cash Flow Automatisé : Monerium et Sablier suppriment la friction manuelle des virements mensuels. Le mécanisme "In-Share" capture la valeur à la source (le Splitter) plutôt que de la réclamer a posteriori.
Résilience Réglementaire : En utilisant Monerium (monnaie électronique régulée) et des wrappers légaux (OpenLaw), le système reste conforme aux réglementations financières (MiCA) tout en conservant l'efficacité de la DeFi.
Scalabilité Opérationnelle : L'utilisation de Kleros et des Oracles Automatisés signifie que RBK n'a pas besoin d'embaucher une armée d'agents de recouvrement. Le code gère le portefeuille ; les humains n'interviennent que dans les cas limites (edge cases).
Ce document ne constitue pas seulement une mise à jour de Livre Blanc ; c'est le plan directeur de la première Dotation Universitaire Autonome (Self-Driving University Endowment).
Sources des citations
How do Safe Smart Accounts work?, consulté le janvier 7, 2026, https://docs.safe.global/advanced/smart-account-overview
SKSudharsanan/4337-wallet: core contract of eip 4337 implementation - GitHub, consulté le janvier 7, 2026, https://github.com/SKSudharsanan/4337-wallet
Account Abstraction Explained: The Future of Web3 Wallets with ERC-4337 | Bitium Blog, consulté le janvier 7, 2026, https://blog.bitium.agency/account-abstraction-explained-the-future-of-web3-wallets-with-erc-4337-853064563e52
The ERC-4337 Tutorial: A Deep Dive into Account Abstraction, consulté le janvier 7, 2026, https://www.ethereum-blockchain-developer.com/advanced-mini-courses/gasless-onboarding-erc2612-erc4337-eip7702/05-erc4337-deep-dive
Safe Modules - Safe Docs, consulté le janvier 7, 2026, https://docs.safe.global/advanced/smart-account-modules
Zodiac Pilot, consulté le janvier 7, 2026, https://pilot.gnosisguild.org/
Zodiac Roles Modifier - Gnosis Guild, consulté le janvier 7, 2026, https://docs.roles.gnosisguild.org/
gnosisguild/role-demo - GitHub, consulté le janvier 7, 2026, https://github.com/gnosisguild/role-demo
0xSplits - protocol breakdown - solidnoob, consulté le janvier 7, 2026, https://www.solidnoob.com/blog/0xSplits
Splits V2 - Docs, consulté le janvier 7, 2026, https://docs.splits.org/sdk/splits-v2
Split acts as an equity instrument by letting you define the percent of future value each recipient will earn. It's a payable smart contract that distributes all ETH & ERC20 tokens it receives among recipients according to pre-set ownership percentages. - Docs, consulté le janvier 7, 2026, https://docs.splits.org/core/split
Gelato Safe Module to automate transactions for Gnosis Safe's - GitHub, consulté le janvier 7, 2026, https://github.com/gelatodigital/gelato-safe-module
Getting Started with Chainlink Automation, consulté le janvier 7, 2026, https://docs.chain.link/chainlink-automation/overview/getting-started
Automating distributions - Splits.org, consulté le janvier 7, 2026, https://splits.org/changelog/automate-distributions/
ERC 3475: The Token Standard That Brings Bonds to the Blockchain - Linum Labs, consulté le janvier 7, 2026, https://www.linumlabs.com/articles/erc-3475-the-token-standard-that-brings-bonds-to-the-blockchain
solv-finance/erc-3525: ERC-3525 Reference Implementation - GitHub, consulté le janvier 7, 2026, https://github.com/solv-finance/erc-3525
Semi-Fungible Tokens: Theory, Standard and Practice v0.9.1 - SFT Labs, consulté le janvier 7, 2026, https://whitepaper.sftlabs.io/SFT%20Whitepaper.pdf
EIP-3525: The Semi-fungible Token - Ethereum Magicians, consulté le janvier 7, 2026, https://ethereum-magicians.org/t/eip-3525-the-semi-fungible-token/9770
Explaining ERC-3525: What it is and How it Works - SFT Labs, consulté le janvier 7, 2026, https://sftlabs.io/2023/01/06/explaining-erc-3525-what-it-is-and-how-it-works/
Obligate: Introduction, consulté le janvier 7, 2026, https://docs.obligate.com/
Top SFT App You Should Know About In 2023, consulté le janvier 7, 2026, https://sftlabs.io/2023/02/06/top-sft-app-you-should-know-about-in-2023/
Monerium: API, consulté le janvier 7, 2026, https://monerium.dev/
Monerium, consulté le janvier 7, 2026, https://monerium.com/
Overview | Monerium - GitHub Pages, consulté le janvier 7, 2026, https://monerium.github.io/js-monorepo/
Log Trigger Upkeep with Chainlink Automation | by Warissara - Medium, consulté le janvier 7, 2026, https://medium.com/@warissara.0039/log-trigger-upkeep-with-chainlink-automation-9d1805a29eda
How To Use Log Trigger Automation | Chainlink Engineering Tutorials - YouTube, consulté le janvier 7, 2026, https://www.youtube.com/watch?v=nMFtqnpb8_k
Best Euro Stablecoin Providers in 2025 - Monerium, consulté le janvier 7, 2026, https://monerium.com/blog/2025/best-euro-stablecoin-providers-2025/
Business terms of service | Monerium, consulté le janvier 7, 2026, https://monerium.com/policies/business-terms-of-service/
Smart contracts at Request Finance, consulté le janvier 7, 2026, https://help.request.finance/en/articles/10123680-smart-contracts-at-request-finance
Onchain invoicing - Request Network, consulté le janvier 7, 2026, https://request.network/onchain-invoicing
Request Network for the Next-Gen Invoicing Solutions, consulté le janvier 7, 2026, https://request.network/blog/request-network-for-the-next-gen-invoicing-solutions
Reclaim Protocol - Identity Tools - Alchemy, consulté le janvier 7, 2026, https://www.alchemy.com/dapps/reclaim-protocol
Reclaim Protocol Docs, consulté le janvier 7, 2026, https://docs.reclaimprotocol.org/
AI to scale zkTLS - Reclaim Protocol, consulté le janvier 7, 2026, https://blog.reclaimprotocol.org/posts/zktls-ai
The zk in zkTLS - Reclaim Protocol, consulté le janvier 7, 2026, https://blog.reclaimprotocol.org/posts/zk-in-zktls
Address: 0x7cc7e125...bdff79127 | Etherscan, consulté le janvier 7, 2026, https://etherscan.io/address/0x7cc7e125d83a581ff438608490cc0f7bdff79127
Dynamic Streams in the Sablier UI, consulté le janvier 7, 2026, https://blog.sablier.com/dynamic-streams-in-the-sablier-ui/
Introducing Sablier V2, consulté le janvier 7, 2026, https://blog.sablier.com/introducing-sablier-v2/
Superfluid — Real-time Token Streaming Protocol (Great for DeFi Hacks) - Medium, consulté le janvier 7, 2026, https://medium.com/@BizthonOfficial/superfluid-real-time-token-streaming-protocol-great-for-defi-hacks-df0dbbb5d11b
Reference implementation of ERC5192 Minimal Soulbound Tokens - GitHub, consulté le janvier 7, 2026, https://github.com/attestate/ERC5192
ERC-5192: Minimal Soulbound NFTs - EIP.tools, consulté le janvier 7, 2026, https://eip.tools/eip/5192
Revocation by Credential Issuer | Learn & Work Ecosystem Library, consulté le janvier 7, 2026, https://learnworkecosystemlibrary.com/glossary/revocation-by-credential-issuer/
Spectral-Finance/challenge-1-modeler-starter-kit - GitHub, consulté le janvier 7, 2026, https://github.com/Spectral-Finance/challenge-1-modeler-starter-kit
RBI MASTER DIRECTIONS ON WILFUL DEFAULTERS: A COMPREHENSIVE GUIDE - Economic Laws Practice, consulté le janvier 7, 2026, https://elplaw.in/wp-content/uploads/2024/08/RBI-Master-Directions-on-Wilful-Defaulters-A-Comprehensive-Guide.pdf
Decentralised Justice and the New York Convention | Kluwer Arbitration Blog, consulté le janvier 7, 2026, https://legalblogs.wolterskluwer.com/arbitration-blog/decentralised-justice-and-the-new-york-convention/
Yellow Paper - Kleros, consulté le janvier 7, 2026, https://kleros.io/yellowpaper.pdf
Whitepapers - Kleros, consulté le janvier 7, 2026, https://kleros.io/whitepaper.pdf
Introducing Kleros Governor: A Smart Contract To Rule Them All, consulté le janvier 7, 2026, https://blog.kleros.io/introducing-kleros-governor/

