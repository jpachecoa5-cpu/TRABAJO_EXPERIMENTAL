ambas       = inscritos_matematica & inscritos_ingles     # {'Luis','Marco'}
solo_mate   = inscritos_matematica - inscritos_ingles     # {'Ana','Sol'}
total       = len(inscritos_matematica | inscritos_ingles)  # 5

print(sorted(ambas), sorted(solo_mate), total)