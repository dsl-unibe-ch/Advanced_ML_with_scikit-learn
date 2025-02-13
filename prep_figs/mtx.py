mtx = np.random.normal(size=(7,7), loc=5)
mtxs = []
for row in mtx:
    rs = [f'{v:.1f}' for v in row]
    print(' '.join(rs))
    mtxs.append('&'.join(rs))
print('@'.join(mtxs))