import { Component } from '@angular/core';
import { NavController} from 'ionic-angular';
import { RecipesPage } from '../recipes/recipes';
import { DomSanitizer} from '@angular/platform-browser';
import { RegistrationPage } from '../registration/registration';
import { IngredientGamePage } from '../ingredient-game/ingredient-game';
import { URLSearchParams, Http, RequestOptions,Headers  } from '@angular/http';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})

export class HomePage {
  baseUrl ="http://localhost:5000/";
  loggedIn = false;
  username;
  password;
  ingredients;
  user ={"name":"","email":"","score":""};
  constructor(public navCtrl: NavController,private http: Http){
  }
  goToRegistration(){
    this.navCtrl.push(RegistrationPage);
  }

  login(){
    let postUrl = this.baseUrl + "login";
        let body = {
            "username" : this.username,
            "password" : this.password
        }
        this.http.post(postUrl,body).subscribe(res =>{
            console.log(res);
            if (res.status == 200){
                alert("Logged in");
                let uid = res.text();
                let id = JSON.parse(uid).id;
                let getUrl= this.baseUrl + "users/"+id;
                this.http.get(getUrl).subscribe(res => {
                  this.user = JSON.parse(res.text());
                });
                if (uid){
                  sessionStorage.setItem('uid',uid);
                }
                this.loggedIn = true;
                console.log(this.loggedIn);
            }
        });
        let getUrl = this.baseUrl + "ingredients";
        this.http.get(getUrl).subscribe(res => {
          this.ingredients = JSON.parse(res.text());
        });
    
  }

  start(){
      console.log(this.ingredients);
      this.navCtrl.push(IngredientGamePage,this.ingredients);
  }
}
