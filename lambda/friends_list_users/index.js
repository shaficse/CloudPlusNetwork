'use strict';

var AWS = require('aws-sdk')
AWS.config.update({ region:'us-east-1' });
var cognito = new AWS.CognitoIdentityServiceProvider()
var userPoolId = 'us-east-1_hSL7PVXdP';
exports.handler = function(event, context, callback){
    console.log('Cognito name = ' + event.cognitoUsername);
    cognito.listUsers({
        UserPoolId: userPoolId,
        AttributesToGet:[],
        Filter:'',
        Limit:60
    }, function(err,data){
        if (err === null){
            var logins = [];
            data.Users.forEach(function(user){
                if(user.Username !== event.cognitoUsername)
                    logins.push(user);
            });
            callback(null,logins);
            
        }else{
            callback(err)
        }
    });
};