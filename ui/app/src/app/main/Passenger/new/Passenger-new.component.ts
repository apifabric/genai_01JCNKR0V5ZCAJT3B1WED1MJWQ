import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Passenger-new',
  templateUrl: './Passenger-new.component.html',
  styleUrls: ['./Passenger-new.component.scss']
})
export class PassengerNewComponent {
  @ViewChild("PassengerForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}