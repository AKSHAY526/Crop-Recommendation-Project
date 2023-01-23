import { Component } from '@angular/core';
import { ServiceService } from './service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'crop';

  constructor(
    private serviceService: ServiceService
    ) { }

      N: any=71;
      P: any=54;
      K: any=16;
      temperature: any=23;
      humidity: any=64;
      ph: any=6;
      rainfall: any=88;
      formValue:any;
 
  // formValue:any;

  onSubmit(form:any){
    this.formValue=form.value;
    console.log(form.value);

    this.getPrice(form.value);
  }

  data:any; 
  getPrice(data: any) {
    return this.serviceService.predict(data).subscribe((response: {}) => {
      let data: any = response;
      this.data=data;
      
      console.log(response);
    });
  }
}
