import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Holiday-new',
  templateUrl: './Holiday-new.component.html',
  styleUrls: ['./Holiday-new.component.scss']
})
export class HolidayNewComponent {
  @ViewChild("HolidayForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}