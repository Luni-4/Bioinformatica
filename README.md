Bioinformatica
================

# Indice

1. [Informazioni](#1-informazioni)
2. [Modalità di lavoro](#2-modalità-di-lavoro)
  1. [Idee](#21-idee)
  2. [Divisione dei compiti](#22-divisione-dei-compiti)
  3. [Link Utili](#23-link-utili)
3. [Input](#3-input)
  1. [Drosophila melanogaster](#31-drosophila-melanogaster)
  2. [Homo sapiens](#32-homo-sapiens)
4. [Output](#4-output)
5. [Dubbi](#5-dubbi)


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

## 2.1. Idee

I numeri associati ai punti rappresentano le priorità di risposta alle domande/esecuzione del lavoro. Più i valori sono bassi, più sono importanti.

1.  Adaboost è necessario per Cesa? Oppure possiamo usare solo SVM e Pegasos? Tu cosa ne pensi? In questo modo lui ci chiederebbe solo SVM, i kernel e l’online gradient descent. La scelta di SVM è obbligata se vogliamo fare Pegasos, visto che è un’implementazione particolare di SVM. Potremmo confrontare i risultati ottenuti da entrambi.
2.  Capire come funziona SVM nello spazio dei kernel RBF, cosa succede al variare dei parametri C e gamma? Fare un’analisi approfondita.
3.  Analizzare i risultati ottenuti con il progetto di bioinformatica, capire perché i nostri risultati sono buoni e valutare se il Boxplot è la scelta adeguata
4.  Finire i grafici che volevi aggiungere per Bioinformatica, Pici
5.  Eliminare gli ill-defined, durante l’orale ho notato che il prof non li aveva compresi perché erano troppo legati alla parte implementativa. Spieghiamo il problema di fondo che porta agli ill-defined.
6.  Cercare di risolvere il problema degli ill-defined scegliendo dei pesi più sensati per le classi
7.  Variare le scale dei grafici, perlopiù le ordinate, almeno abbiamo dei risultati più fighi in visualizzazione
8.  Pulire il codice in alcuni punti, se fosse possibile. 
9.  Correggere gli errori grammaticali e le frasi legnose del report
10. Le curve roc e prc le facciamo? Oppure ce ne freghiamo e andiamo avanti? Sarebbe bello perderci un po' di tempo per capire come funzionano. 

## 2.2. Divisione dei compiti

FEDERICO:

- Punti 4 e 8

MICHELE:

- Vorrei occuparmi del punto 2 e del punto 7

## 2.3. Link Utili

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

- Tanti grafici che mostrino il nostro operato
- Dei buoni confronti tra i classificatori
- Un buon report

# 5. Dubbi

FEDERICO:

MICHI:
