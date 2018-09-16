import { Component } from '@angular/core';
import {NavController, NavParams } from 'ionic-angular';
import { URLSearchParams, Http, RequestOptions,Headers  } from '@angular/http';
/**
 * Generated class for the BadgeCollectionPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */


@Component({
  selector: 'page-badge-collection',
  templateUrl: 'badge-collection.html',
})
export class BadgeCollectionPage {
  baseUrl ="http://localhost:5000/";
  badges=[{"id":"","name":"","image":""}];
  constructor(public navCtrl: NavController, public navParams: NavParams, private http: Http) {
    let user = JSON.parse(sessionStorage.getItem('uid'));
    let user_id = user.id;
    let getUrl = this.baseUrl+"users/"+user_id+"/badges";
    http.get(getUrl).subscribe(res => {
      let items = JSON.parse(res.text()).badges;
      for (let i = 0; i < items.length; i++){
        let getUrl = "https://rickandmortyapi.com/api/character/" + items[i].extid;
        http.get(getUrl).subscribe( res => {
          let b = JSON.parse(res.text());
          this.badges.push(b);
        });
      }
    });
    this.badges.splice(0,1);
  }

}
