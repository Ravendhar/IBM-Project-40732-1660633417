from flask import Flask,redirect,request,render_template,url_for,session
import ibm_db
import re 

app=Flask(__name__)
app.secret_key='a'
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ygg09863;PWD=dQXLECjtaCqXsJUt;","","")

if __name__=="__main__":
    app.run(host='0.0.0.0')