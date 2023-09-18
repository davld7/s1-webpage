from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def root():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Origen del Internet</title>
        <style>
            body {
                background-color: #f2f2f2;
                font-family: Arial, sans-serif;
                margin: 0;
            }
            h1 {
                color: #333;
                text-align: center;
            }
            p {
                color: #666;
                font-size: 18px;
                line-height: 1.5;
                margin-left: 20px;
                margin-right: 20px;
            }
            ul {
                color: #006699;
                list-style-type: square;
                margin-left: 30px;
            }
            hr {
                border-color: #006699;
            }
            footer {
                text-align: right;
                font-style: italic;
                margin-top: 20px;
                margin-right: 20px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <h1>Origen del Internet</h1>
        <hr />
        <p><strong>Introducción a Internet:</strong></p>
        <p>Internet es una red global de computadoras interconectadas que permite la comunicación y el intercambio de información entre personas de todo el mundo. Surgió como un proyecto militar en los Estados Unidos en la década de 1960, con el objetivo de crear una red de comunicación robusta y descentralizada que pudiera resistir posibles ataques durante la Guerra Fría. El primer mensaje enviado a través de ARPANET, la precursora de Internet, fue "LOGIN".</p>
        <p><strong>Desarrollo y Evolución:</strong></p>
        <p>El desarrollo de Internet ha sido constante a lo largo de las décadas. A partir de ARPANET, la primera red de conmutación de paquetes se expandió a nivel académico y de investigación en los años 70. En los 90, Internet se convirtió en una red pública de acceso global y su uso se popularizó rápidamente. La invención del World Wide Web por Tim Berners-Lee en 1989 fue un hito crucial para la accesibilidad y expansión de Internet.</p>
        <p><strong>Impacto en la Sociedad:</strong></p>
        <p>Internet ha revolucionado la forma en que vivimos, comunicamos, trabajamos y accedemos a la información. Ha conectado a personas de todo el mundo y ha generado cambios significativos en la sociedad moderna. Ha facilitado la comunicación instantánea, el comercio electrónico, la educación en línea y mucho más. Además, ha democratizado el acceso a la información, permitiendo que prácticamente cualquier persona tenga acceso a conocimientos y recursos antes inaccesibles.</p>
        <hr />
        <footer>Elaborado por: Roberto David Morales Ramos</footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html)
