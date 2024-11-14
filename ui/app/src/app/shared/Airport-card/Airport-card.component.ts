import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Airport-card.component.html',
  styleUrls: ['./Airport-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Airport-card]': 'true'
  }
})

export class AirportCardComponent {


}