import { Component } from '@angular/core';
import {NavController, NavParams } from 'ionic-angular';
import { URLSearchParams, Http, RequestOptions,Headers  } from '@angular/http';
import { HomePage } from '../home/home';
/**
 * Generated class for the RegistrationPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

  
@Component({
  selector: 'page-registration',
  templateUrl: 'registration.html',
})
export class RegistrationPage {
  name;
  username;
  email;
  password;
  baseUrl ="http://localhost:5000/";
  constructor(public navCtrl: NavController, public navParams: NavParams, private http: Http) {
  }

  create(){
    let postUrl = this.baseUrl+"users";
        let body = {
            "name": this.name,
            "username": this.username,
            "email": this.email,
            "password": this.password
        }
        this.http.post(postUrl,body).subscribe(res => {
            if (res.status == 200){
                alert("Successfully created account");
                this.navCtrl.push(HomePage);
            }else{
                alert("User already exist");
            }
          }
        );
  }
}
