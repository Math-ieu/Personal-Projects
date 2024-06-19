from django.shortcuts import render
from portfolio.forms import mainForm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def envoyer_email(destinataire, sujet, contenu):
    # Configurer les détails du compte d'envoi
    expediteur = "assouakakpo69@gmail.com"
    mot_de_passe = 'zlgxjvcwixtulqfy'

    # Créer l'objet MIMEMultipart pour le message
    message = MIMEMultipart()
    message["From"] = expediteur
    message["To"] = destinataire
    message["Subject"] = sujet

    # Ajouter le contenu du message
    message.attach(MIMEText(contenu, "plain"))

    # Établir une connexion avec le serveur SMTP
    serveur_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    serveur_smtp.starttls()

    # S'authentifier avec les identifiants du compte d'envoi
    serveur_smtp.login(expediteur, mot_de_passe)

    # Envoyer le message
    serveur_smtp.send_message(message)

    # Fermer la connexion avec le serveur SMTP
    serveur_smtp.quit()


def main(request):
    form = mainForm()
    register = mainForm(request.GET)
    if register.is_valid():
        fname = register.cleaned_data['fname']
        lname = register.cleaned_data['lname']
        email = register.cleaned_data['email']
        msg = register.cleaned_data['message']

        sbjct = f"Message de Mr/Mme {fname} {lname} d'adresse mail: {email}"
        envoyer_email("developpeurmathmathieu@gmail.com", sbjct, msg)
        return render(request, 'index.html', {'form':form})
  
    return render(request, 'index.html', {'form':form})

