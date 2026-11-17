# Capital Bot V2

Bot Discord mínimo, funcional e independente de templates externos. Usa comandos de barra: `/ping` e `/ajuda`.

## Hospedagem Altare
- Runtime: Python 3.13
- Diretório raiz: `./`
- Comando de instalação: `pip install -r requirements.txt`
- Comando de inicialização: `python bot.py`
- Variáveis: `TOKEN` (obrigatória); `GUILD_ID` (recomendada, ID numérico do servidor de Discord)
- `GUILD_ID` sincroniza comandos imediatamente no servidor indicado. Sem ela, usa sincronização global (pode demorar para aparecer).

No Discord Developer Portal, autorize o bot com `bot` e `applications.commands`. Não é preciso ativar `Message Content Intent` para estes comandos.

Não coloque o token no GitHub, em arquivos de código ou mensagens. Configure apenas nas variáveis secretas da Altare.

**Atenção:** se a V1 e a V2 usarem o mesmo TOKEN, desligue a V1 antes de ligar a V2 para evitar duas conexões simultâneas do mesmo bot.
