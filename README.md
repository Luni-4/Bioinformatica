Bioinformatica
================

# Indice

1. [Informazioni](#1-informazioni)
2. [Modalità di lavoro](#2-modalità-di-lavoro)
  1. [Divisione dei compiti](#21-divisione-dei-compiti)
  2. [Link Utili](#22-link-utili)
3. [Input](#3-input)
  1. [Drosophila melanogaster](#31-drosophila-melanogaster)
  2. [Homo sapiens](#32-homo-sapiens)
4. [Output](#4-output)
5. [Idee](#5-idee)
6. [Dubbi](#6-dubbi)
7. [Creazione Grafici](#7-creazione-grafici)


-----------------

# 1. Informazioni

- Linguaggio di programmazione: Python
- Versione Python: 3.5
- Librerie Python
    - scikit-learn
    - numpy
    - scipy
    - matplotlib
    - python3-tk (sudo apt-get install python3-tk) 

# 2. Modalità di lavoro

## 2.1. Divisione dei compiti

FEDERICO:

- Non usare i punti nel filename dei grafici perché latex non riesce a caricarli - FATTO, uso il trattino (-)
- Eliminare la fscore0 presente nei grafici del livello 1 di tutti i classificatori di tutte le ontologie - FATTO, solo quella è da eliminare?
- Allargare tutti i grafici: evitare di tagliare le etichette delle configurazioni di classificatori - FATTO
- mettere a posto la scala delle ordinate (in alcuni grafici non sono ben allineate)
- Fare i grafici prc e roc con la stessa modalità adottata al livello 2 ---> teniamolo opzionale per mancanza di tempo visto che non ce l'ha richiesto
- Mettere a posto AdaBoost sul report, ovvero cerca di renderlo più simile possibile a svm del report
- Mettere a posto le proporzioni dei grafici ill-defined
- Spiegare il funzionamento dei grafici (posso farlo io domani, se non ce la fai)

- Ho pensato al livello 3, direi che possiamo lasciarlo così come è adesso. Fare la media della media non contribuisce per niente al classificatore,
perché come hai detto si perdono informazioni. Per cui non tocchiamolo più e lasciamolo così. Migliora solo la parte grafica, soffre anche lui dei problemi
spiegati sopra.

MICHELE:

- Rileggere il documento e correggere gli errori

## 2.2. Link Utili

- Dati: http://homes.di.unimi.it/valentini/DATA/ProgettoBioinf1617

- Specifiche progetto Valentini: https://homes.di.unimi.it/valentini/SlideCorsi/Bioinformatica1617/Bioinf-Project1617.pdf

- Salvataggio dei classificatori come oggetti: http://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/

- Buona spiegazione di AUPRC e AUROC: http://www.chioka.in/differences-between-roc-auc-and-pr-auc/

- Spiegazione sbilanciamento delle classi (Data Imbalance) e possibili metodi per risolverlo: http://www.chioka.in/class-imbalance-problem/

- Spiegazione Precision-Recall Curve su Quora: https://www.quora.com/What-is-Precision-Recall-PR-curve?share=1

- Metodi di scoring: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

- Precision-Recall-Curve: https://classeval.wordpress.com/introduction/introduction-to-the-precision-recall-plot/

- ROC e AUROC: http://www.cs.bris.ac.uk/~flach/ICML04tutorial/ 

- Metriche per classificatori binari, multiclasse, multi-label: http://rali.iro.umontreal.ca/rali/sites/default/files/publis/SokolovaLapalme-JIPM09.pdf


# 3. Input

- OGNI ENTRY DELLA MATRICE É SEPARATA DA UN ALTRA PER MEZZO DI UN TAB
- TENIAMO A 0 I VALORI DELLE DIAGONALI DELLE MATRICI DI ADIACENZA (FINGIAMO CHE NON ESISTANO)


## 3.1. Drosophila melanogaster

- Matrice di adiacenza 3195 x 3195.Un entry della matrice contiene un valore che indica la similarità tra le proteine, individuate dagli indici della entry stessa.

- Matrice delle annotazioni. Un entry della matrice può assumere solo i valori 0 e 1. Il valore 0 significa che la proteina non è associata alla classe, al contrario con 1 la proteina è associata.
    - 3195 x 1951 per BP
    - 3195 x 234 per MF
    - 3195 x 235 per CC

## 3.2. Homo sapiens

- Matrice di adiacenza 19247 x 19247. Un entry della matrice contiene un valore che indica la similarità tra le proteine, individuate dagli indici della entry stessa.

- Matrice delle annotazioni. Un entry della matrice può assumere solo i valori 0 e 1. Il valore 0 significa che la proteina non è associata alla classe, al contrario con 1 la proteina è associata.
    - 19247 x 3958 per BP
    - 19247 x 899 per MF
    - 19247 x 601 per CC

# 4. Output

- Usare una 5-fold cross-validation per generare il training set e i test set, a partire dalle matrici di adiacenza e delle annotazioni in input.

- Provare diverse soglie t di accettazione secondo un determinato criterio (??).

- Calcolare la Precisione (Prec(t)) e la sensibilità (Rec(t)) per le soglie t stabilite precedentemente. Cercare delle librerie che consentono di calcolarle

- Calcolare la F-score gerarchica (convertire in python il file F-hier.R, scritto in R, altrimenti usare una funzione di una libreria per calcolarla)

# 5. Idee

- Cercare una buona implementazione di Pegaso, possibilmente ottimizzata il più possibile
- SVM normali
- SVM con class_weight=‘balanced’
- Approfondire parametro C nelle SVM
- AdaBoost
- Adaboost con diversi parametri o classificatori (quali?)
- Fare grafici che mostrano come variano diverse metriche in funzione di quanto sono popolate le classi.

# 6. Dubbi

FEDERICO:

MICHI:

SVM parametri

Kernel RBF trasforma i dati in input dallo spazio delle feature in uno spazio kernel composto da gaussiane. Un link che spiega bene come funziona
è questo https://calculatedcontent.com/2012/02/06/kernels_part_1/ più la pagina di Wikipedia https://en.wikipedia.org/wiki/Radial_basis_function_kernel

Gamma: corrisponde all'inverso del raggio di influenza che determina quali campioni sono selezionati dal modello come support vectors. Con valori piccoli il
raggio è molto grande, con valori alti il raggio è molto piccolo.

Parametro C: parametro di tradeoff tra capacità di classificare al meglio gli esempi del training set (modello più complesso) e semplicità della funzione di decisione
(modello più semplice). Un C basso comporta una funzione di decisione più semplice e quindi un modello più semplice, mentre un C alto mira a classificare al meglio
tutti gli esempi del training set (potrebbe overfittare). C alti comporta una maggiore libertà del modello nel scegliere gli esempi per il support vector

Svm è molto sensibile al parametro gamma. 

Se gamma è troppo grande, il raggio di influenza è troppo piccolo e questo significa che il support vector
conterrà solo gli esempi sul margine o quelli che violano il vincolo, ovvero il support vector stesso. In questo modo, qualsiasi sia il valore di C, l'overfitting è
assicurato.

Quando gamma è troppo piccolo, il raggio di influenza è tropp grande. Il support vector è composto da tutti gli esempi del training set. Il modello
risulta troppo "vincolato" e quindi non riesce a ottenere la forma della funzione discriminante. (modello simile a quello lineare)

I valori migliori si trovano sulla diagonale tra C e gamma.

Delle buone configurazioni potrebbero essere:

-  Configurazione 1
    - Kernel: RBF 
    - Gamma basso (tanti esempi nel support vector) 
    - Valori di C grandi (C sceglie più liberamente gli esempi da mettere come support vector)

-  Configurazione 2
    - Kernel: RBF 
    - Gamma medio (default) 
    - Valori di C bassi (limitare la scelta dei support vectors e trovare un predittore con meno memoria e più velocemente)
    
C_range = [-2, 10]
gamma_range = [-9, 3, 13]

I range degli esempi sono dati in scala logaritmica in questo modo

C_range = np.logspace(-2, 10, 13)
gamma_range = np.logspace(-9, 3, 13)



Kernel lineari: da scartare, in quanto non sappiamo se abbiamo training set linearmente separabili

Kernel polinomiali: direi di provare a usare un degree (parametro ignorato dagli altri kernel) compreso tra 3 e 5. Usare valori più alti comporterebbe
un elevato tempo di computazione.

-  Configurazione 3
    - Kernel: Poly
    - Degree: [3,5] 
    - Gamma basso (tanti esempi nel support vector) 
    - Valori di C grandi (C sceglie più liberamente gli esempi da mettere come support vector)

-  Configurazione 4
    - Kernel: RBF
    - Degree: [3,5] 
    - Gamma medio (default) 
    - Valori di C bassi (limitare la scelta dei support vectors e trovare un predittore con meno memoria e più velocemente)
    
# 7. Creazione Grafici

-  Livello 1 (Analisi delle configurazioni di classificatori)
    - Per ogni ontologia (CC, MF)
    - Per ogni famiglia (ada, svm) 
    - Per ogni metrica (auroc, auprc, fscore1) --> precision, recall facoltativi 

Ogni classificatore avrà 3 istogrammi (uno per ogni metrica) di 3 colonne l'uno. Le colonne rappresentano 3 configurazioni di parametri diversi e l'altezza delle colonne
dipenderà dal valore della metrica considerata.

Totale: 12 grafici 

Non confrontare tra loro classificatori diversi! I grafici devono contenere colonne associate allo stesso classificatore!!!

-  Livello 2 (Analisi dei classificatori sulle classi ---> scegliere la configurazione migliore risultante dal livello 1)
    - Per ogni ontologia (CC, MF)
    - Per ogni famiglia (ada, svm) 
    - Per fscore1, precision1, recall1

Scegliere tra le classi delle ontologie quelle con un buon numero di positivi e alcune molto sbilanciate. Confrontare tra loro la precision, recall, fscore della stessa
classe (metodo degli istogrammi vicini, come ho inviato nella foto su whatsapp). Fare tanti grafici quante sono le classi per il quale si vuole fare il confronto.
Calcolare per queste classi anche la roc e la prc e valutarne la auroc e auprc. Auroc e Auprc valutate come istogrammi, mentre roc e prc con le loro curve, direi di metterle tutte in un unico grafico,
come su scikit-learn

-  Livello 3 (Confronto classificatori ---> configuarazione migliore livello 1)
    - Per ogni ontologia (CC, MF)
    - Per ogni famiglia (ada, svm) 
    
In questo livello si usa il grafico di Pici, già creato. 
Confrontare AdaBoost e Svm, con le configurazioni migliori, sulle migliori classi sbilanciate e le miglori classi ricce di positivi. Fare 2
grafici. Uno per la classe positiva e una per la classe negativa





