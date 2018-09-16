import { Component } from '@angular/core';

import { AboutPage } from '../about/about';
import { ContactPage } from '../contact/contact';
import { HomePage } from '../home/home';
import { BadgeCollectionPage} from '../badge-collection/badge-collection';

@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {

  tab1Root = HomePage;
  tab2Root = BadgeCollectionPage;
  tab3Root = ContactPage;

  constructor() {

  }
}
