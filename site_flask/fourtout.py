<h1>{{ self.titre() }}</h1>





#ajout fichier:
fichier = request.files['fichier']
                nom_fichier = fichier.filename
                if nom_fichier[-5:] != '.html':
                        nom_fichier = secure_filename(nom_fichier)
                        fichier.save('./uploads/' + nom_fichier)




#test checkbox:
if request.form.getlist('check'):