library(tidyverse)
library(lubridate)

dados = dados_brutos |>
  dplyr::select(time_path)

dado = sapply(dados, as.character)

hora = str_sub(dado, 3, 7)  #Strings apenas com horas

dad = sapply(hora, as.data.frame)

posix = strftime(strptime(hora, format = "%H:%M"), format = "%H%M") #tira o : do character

tempo = as.numeric(posix) #transforma o dado em numérico

par(mfrow=c(2,2))

hist(tempo, breaks = 24, col = "blue", xlim = c(0,2500), main="Frequência da hora de acesso")


dado1 = dados_brutos |> 
  dplyr::select(day)

dia_cont = table(dado1)

#Finais de semana de março = 2,3,9,10,16,17,23,24,30,31

finaisdesemana = c(tempo[114:161], tempo[736:788], tempo[1417:1446], tempo[2420:2452]) #Separação de fins de semana
diassemanaremov = which(tempo %in% finaisdesemana)
diassemana = tempo[-diassemanaremov]


hist(finaisdesemana, breaks=24, col ="red", xlim = c(0,2500), main = "Final de semana")
hist(diassemana, breaks=24, col ="green", xlim = c(0,2500), main = "Dias de semana")
