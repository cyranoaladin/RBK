Addendum Technique RBK 3.0 : Infrastructure Financière Haute-Fréquence sur Solana
1. Introduction Stratégique : L'Avantage de la Vitesse et du Coût
La migration de l'infrastructure RBK vers Solana permet de passer d'un modèle "Code-as-Law" (EVM) à un modèle de "Finance Haute-Fréquence". Contrairement à Ethereum où les coûts de gaz limitent l'automatisation des micro-paiements, l'architecture de Solana (Proof-of-History, Sealevel) permet un streaming monétaire continu et une gestion de compte (Account Abstraction) native à des coûts négligeables.
Cette documentation remplace les standards ERC par les Extensions Token-2022, les contrats intelligents par des Programmes SPL, et les multisigs Gnosis par Squads V4.
2. Protocole "In-Share" 90/10 : Gestion de Trésorerie Programmable (Phase de Formation)
Sur Solana, la gestion des fonds partagés ne repose pas sur des contrats déployés individuellement, mais sur des comptes dérivés de programmes (PDAs) stateless, offrant une sécurité et une performance accrues.
2.1 Le Coffre-Fort Numérique : Squads V4 (Multisig)
Au lieu de Safe, nous utilisons Squads V4, le standard de facto pour la gestion de trésorerie sur Solana, sécurisant plus de 10 milliards de dollars d'actifs.
Architecture du Squad : Chaque apprenant reçoit un "Squad" (Multisig) 2-sur-3 lors de l'onboarding.
Clé Apprenant (Member) : Peut initier des transactions.
Clé RBK (Guardian) : Doit co-signer pour valider ou rejeter.
Clé de Récupération (Oracle/Escrow) : Pour la récupération sociale en cas de perte de clé.
Fonctionnalité Clé : "Spending Limits" : Squads intègre nativement des limites de dépenses. RBK peut configurer le Squad pour permettre à l'apprenant de retirer seul ses 10% (via une Spending Limit récurrente), tout en bloquant cryptographiquement tout transfert supérieur sans la signature de RBK.
2.2 Le Moteur de Ventilation : Metaplex Hydra (Fanout Wallet)
Sur Solana, le modèle de transaction est "Pull" (tirer) et non "Push". Pour diviser les revenus automatiquement, nous utilisons le Fanout Wallet (Hydra) de Metaplex.
Mécanisme de "Staged Split" :
Réception : Le Fanout Wallet reçoit les fonds (SOL, USDC, EURC) provenant des Bounties ou Grants.
Pool de Répartition : Les fonds ne sont pas envoyés immédiatement. Ils s'accumulent dans le compte du programme Hydra.
Distribution (Crank) : Un bot d'automatisation (hébergé sur Helius ou Clockwork) appelle la fonction distribute périodiquement.
Règlement : Le programme calcule les parts (90% RBK, 10% Apprenant) et les envoie aux Associated Token Accounts (ATA) respectifs.
Avantage : Contrairement à un Splitter EVM qui nécessite souvent une transaction complexe par paiement, Hydra gère efficacement la fragmentation des tokens SPL sans bloquer les fonds.
3. Architecture ISA Smart-Contract : Token-2022 (Phase Post-Formation)
L'innovation majeure de Solana est Token-2022 (Token Extensions). Ce standard permet d'intégrer des règles complexes (intérêts, transferts restreints, confidentialité) directement au niveau du token, sans avoir besoin d'envelopper (wrap) le token dans un contrat intelligent externe.
3.1 Tokenisation de la Dette : Mint avec "Transfer Hooks"
Le contrat ISA est représenté par un Token-2022 unique minté pour l'apprenant.
Extension "Transfer Hook" : Cette extension force chaque transfert du token à passer par un programme de validation logique.
Règle : Le token de dette est Intransférable (Soulbound) sauf vers l'adresse de "Burn" (remboursement).
Application : Si l'apprenant essaie d'envoyer ce token à un autre wallet pour cacher sa dette, le Transfer Hook rejette la transaction au niveau du protocole.
Extension "Metadata Pointer" : Stocke les données dynamiques de la dette (Montant Restant, Cap, Taux d'Intérêt) directement sur la chaîne, lisibles par n'importe quel wallet Solana (Phantom, Solflare).
Extension "Interest-Bearing" : Si l'ISA inclut un taux d'intérêt, le solde de la dette peut s'ajuster algorithmiquement à chaque bloc, offrant une visualisation en temps réel de l'obligation financière.
4. Flux de Remboursement et Streaming : Streamflow & Helio
4.1 Streaming de Salaire : Streamflow
Pour le remboursement, nous utilisons Streamflow, le protocole de streaming natif le plus robuste sur Solana.
Logique de Paiement : Dès que l'apprenant reçoit son salaire (en USDC/EURC), un flux est créé via le SDK Streamflow.
Vesting Inversé : Au lieu de "vesting" (recevoir des tokens), l'apprenant configure un flux de paiement vers RBK.
Fréquence : Le paiement est streamé chaque seconde. Cela lisse la sortie de trésorerie pour l'apprenant et assure une entrée constante pour RBK.
Annulabilité : Le flux peut être annulé par l'apprenant (arrêt de l'emploi), ce qui déclenche une alerte immédiate (voir Section 6).
4.2 Paiements Web2/Web3 : Helio & Kast
Pour l'On-Ramp (conversion Fiat -> Crypto), Solana dispose d'outils spécifiques :
Kast (Virtual Accounts) : Kast fournit des comptes bancaires virtuels (IBAN/ACH) qui convertissent automatiquement les dépôts Fiat en stablecoins (USDC) sur Solana. C'est l'équivalent direct de Monerium sur Solana.
Helio (Pay Links) : Pour les freelances, Helio permet de générer des liens de paiement. Les clients paient en CB ou Crypto, et Helio route automatiquement la part de RBK (15%) vers le Treasury Wallet, et le reste vers l'apprenant, agissant comme un Splitter à la source.
4.3 Vérification des Revenus : Reclaim Protocol (zkTLS)
Comme sur EVM, Reclaim Protocol est compatible Solana. Il permet à l'apprenant de générer une preuve Zero-Knowledge de son compte bancaire traditionnel (Biat, Revolut) pour prouver ses revenus sans révéler ses transactions. Le contrat Solana vérifie cette preuve on-chain pour valider la conformité.
5. Identité et Réputation : Le SBT Natif (Token-2022)
Sur Solana, pas besoin de standard complexe comme l'ERC-5192. Token-2022 possède des extensions natives pour cela.
5.1 Le Diplôme : Extension "Non-Transferable"
Le diplôme RBK est un Token-2022 avec l'extension Non-Transferable activée au minting.
Propriété : Il réside dans le wallet de l'apprenant.
Restriction : Le protocole interdit tout transfert (instruction Transfer désactivée). Il est littéralement "collé" au wallet.
5.2 Le "Kill Switch" : Extension "Permanent Delegate"
C'est l'arme de dissuasion massive de RBK. Lors du minting du SBT, RBK se désigne comme Permanent Delegate.
Pouvoir : Cette extension donne à RBK le pouvoir absolu de Brûler (Burn) ou Transférer (Saisir) le token depuis le wallet de l'apprenant, sans sa signature.
Application : En cas de défaut de paiement avéré (après arbitrage), le contrat appel l'instruction Burn via le Permanent Delegate. Le diplôme disparaît instantanément du wallet de l'apprenant.
6. Gouvernance et Arbitrage : Realms & Squads
6.1 Gouvernance DAO : SPL Governance (Realms)
Toute modification des paramètres de l'ISA (ex: changer le % de prélèvement global) passe par Realms, l'interface de gouvernance de Solana. Les décisions sont exécutées on-chain.
6.2 Arbitrage Décentralisé
Solana n'a pas encore de cour Kleros native aussi mature qu'Ethereum. Nous proposons une approche hybride :
Niveau 1 : Comité de Sages (Squads Multisig). Un Squad composé d'alumni vérifiés et de membres du board RBK agit comme tribunal de première instance.
Niveau 2 (Optionnel) : Utilisation d'un pont (Wormhole) pour envoyer le litige vers Kleros sur Ethereum, mais cela ajoute de la complexité. Le modèle "Conseil des Alumni" via Realms est préférable pour rester dans l'écosystème Solana rapide et peu coûteux.
7. Synthèse des Outils Solana
Fonctionnalité
Outil EVM (Ancien)
Outil Solana (Nouveau)
Avantage Solana
Multisig Wallet
Gnosis Safe
Squads V4
Comptes stateless, UX supérieure, Spending Limits natifs.
Revenue Split
0xSplits
Metaplex Hydra (Fanout)
Gestion native du modèle "Pull" de Solana.
Dette Token
ERC-3525
Token-2022 (Transfer Hook)
Enforcement des règles directement dans le standard du token.
Streaming
Sablier
Streamflow
Streaming à la seconde avec frais négligeables (<0.0001$).
Fiat On-Ramp
Monerium
Kast / Helio
Comptes virtuels intégrés et liens de paiement crypto-natifs.
Diplôme SBT
ERC-5192
Token-2022 (Non-Transferable)
Pas de contrat custom, extension standardisée et audité.
Révocation
Fonction Custom
Token-2022 (Permanent Delegate)
Contrôle absolu et standardisé pour l'émetteur (RBK).

8. Argumentaire Technique pour le CEO (Version Solana)
"Migrer cette infrastructure sur Solana ne nous fait pas seulement économiser des frais de gaz ; cela nous donne des super-pouvoirs de contrôle. Avec Token-2022, nous n'avons pas besoin d'écrire des contrats complexes qui peuvent être hackés ; nous utilisons des extensions natives du protocole pour créer des diplômes qui sont techniquement impossibles à transférer mais que nous pouvons techniquement supprimer à distance via le Permanent Delegate. C'est le niveau de contrôle d'une base de données centralisée avec la transparence et la sécurité d'une blockchain publique."

