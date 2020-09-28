with open('chic2_.txt', 'r') as chic, open('chic2-Merged.txt', 'r') as Seq:
    seq = chic.readlines()
    sequence = []
    for i in range(len(seq)):
        line = seq[i].rstrip('\n')
        for j in range(len(line)):
            sequence.append(line[j])

    count = len(sequence)
    last = count - 500

    lastSeq = []
    for i in range(last, count):
        lastSeq.append(sequence[i])

    upstream = set()
    downstream = set()
    exons = set()
    introns = set()

    for i in range(500):
        upstream.add(i + 1)

    for i in range(last, count):
        downstream.add(i + 1)

    for i in range(500, count-500):
        if sequence[i] in ['A', 'G', 'T', 'C']:
            exons.add(i + 1)
            # print(i+1)
        else:
            introns.add(i + 1)

    repeatSeq = Seq.readlines()
    RepeatsRegions = set()
    InExonsNum = 0
    InIntronsNum = 0
    UpNum = 0
    DownNum = 0
    for i in range(2, len(repeatSeq)):  #для g4hunter первое число отрезка на 2
        line = repeatSeq[i].rstrip('\n').replace('\t', ' ').split(' ')
        # print(line)
        region = set()
        #print(line)
        for j in range(int(line[0]), int(line[3])+1):  # for g4hunter change number на 0, 3
            #for other 3,4
            region.add(j)
        #print(region)
        if len(exons.intersection(region)) > 0:
            InExonsNum += 1
        elif len(introns.intersection(region)) > 0:
            InIntronsNum += 1
        elif len(upstream.intersection(region)) > 0:
            UpNum += 1
        elif len(downstream.intersection(region)) > 0:
            DownNum += 1

        #print(InExonsNum, InIntronsNum, UpNum, DownNum)
    print('Exons:', InExonsNum, 'Introns:', InIntronsNum, 'Upstream:', UpNum, 'Downstream:', DownNum)
    #for i in range(301, 315):
    #    test.add(i)
    #if upstream.isdisjoint(test):
    #    print('zbs')

    #print(len(test.intersection(upstream)))
            #print(j)
            #RepeatsRegions.add(j)
        # for j in range(len(line)):
        #    sequence.append(line[j])

    #print(len(sequence))
    #print(len(repeatSeq))
    #print(len(RepeatsRegions))

