import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Passenger-card.component.html',
  styleUrls: ['./Passenger-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Passenger-card]': 'true'
  }
})

export class PassengerCardComponent {


}