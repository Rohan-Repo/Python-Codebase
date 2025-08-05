from flask import Flask, request, redirect, json, jsonify, render_template

app = Flask(__name__)

def getCompanyRating(company):
    return company.get('rating')

@app.route( '/' )
def showLoginPage():
    return render_template( 'Login.html' )

@app.route( '/api/login', methods=['POST'] )
def userLogin():
    adminUserName = request.form.get("inpUserName")
    adminPassword = request.form.get("inpPassword")

    print( adminUserName, ' / ', adminPassword )

    with open('resources/AdminUsers.json') as jsonFile:
        parsedAdminJSON = json.load(jsonFile)
        print( parsedAdminJSON )

        for user in parsedAdminJSON:
            print( 'u : ', user )
            if adminUserName == user['userName'] and adminPassword == user['password'] and user['userActive'] == True:
                with open('resources/CanadianCompanies.json') as jsonFile:
                    parsedCompanyJSON = json.load(jsonFile)
                    # Sort Data in Descending order of Company Rating
                    # parsedCompanyJSON.sort( key=getCompanyRating, reverse=True )
                    return render_template( 'CompanyDashboard.html', plcCompanyInfo=parsedCompanyJSON )
                    # return jsonify( respCode =  200, companyData = parsedCompanyJSON  )
            
        # If No User Found then Show Login Error Page
        return render_template( 'LoginErrorPage.html' )