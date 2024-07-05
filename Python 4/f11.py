def valorVeiculo(vv, ve, tx,qp):
    vse = vv - ve
    vp = vse / qp
    vj = 0
    for i in range(0,qp):
        vj += tx * vv
    vt = (qp*vp) + vj + ve
    print(f"Valor Total: R$ {vt:.2f}")
    print(f"Valor de cada parcela: R$ {vp:.2f}")
    print(f"Valor total dos juros: R$ {vj:.2f}")

valorVeiculo(100,10,0.1,3)