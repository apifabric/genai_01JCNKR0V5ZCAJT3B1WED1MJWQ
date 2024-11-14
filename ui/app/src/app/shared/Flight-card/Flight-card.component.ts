import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Flight-card.component.html',
  styleUrls: ['./Flight-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Flight-card]': 'true'
  }
})

export class FlightCardComponent {


}