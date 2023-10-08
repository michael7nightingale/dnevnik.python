<script>
import {getMarks} from "@/services/Marks";
import {getUser} from "@/services/Auth";
import {getSubjects} from "@/services/Subjects";


export default{
  name: "MarksView",
  data(){
    return {
      marks: null,
      subjects: null,
      marksTable: null
    }
  },

  mounted() {
    let user = getUser();
    if (!user){
      window.location = this.$router.resolve({name: "login"}).fullPath;
    }
    getSubjects()
        .then((response) => {
          this.subjects = response.data;
        })
        .then(() => {
            getMarks()
              .then((response) => {
                  this.marks = response.data;
              })
              .then(() => {
                   let marksTableProxy = {};
                   for (let subject of this.subjects){
                     marksTableProxy[subject.id] = {
                       name: subject.subject.name,
                       marks: []
                     }
                   }
                   for (let mark of this.marks){
                      marksTableProxy[mark.lesson.study_group_subject_id].marks.push(mark.mark);
                   }
                   this.marksTable = marksTableProxy;
              })
          }
        );

  },
  methods: {
    countAverage(numbers){
      if (numbers.length === 0) return ""
      let sum = 0;
      for (let number of numbers){
        sum += number;
      }
      return sum / numbers.length
    }
  }

}
</script>

<template>
<div v-if="marks && subjects">
  <section class="w-100 p-4 justify-content-center">
<!--      <div class="row justify-content-start" id="filter-sort-example-filters" data-mdb-auto-filter="true">-->
<!--        <div class="col-md-6" data-mdb-filter="color">-->
<!--          <span class="fa-lg">Filter: Color</span>-->

<!--          <div class="form-check mt-3">-->
<!--            <input class="form-check-input" type="radio" name="filterSortRadioOptions" id="filterSortRadio1" value="black">-->
<!--            <label class="form-check-label" for="filterSortRadio1">Black</label>-->
<!--          </div>-->

<!--          <div class="form-check">-->
<!--            <input class="form-check-input" type="radio" name="filterSortRadioOptions" id="filterSortRadio2" value="red">-->
<!--            <label class="form-check-label" for="filterSortRadio2">Red</label>-->
<!--          </div>-->

<!--          <div class="form-check">-->
<!--            <input class="form-check-input" type="radio" name="filterSortRadioOptions" id="filterSortRadio3" value="blue">-->
<!--            <label class="form-check-label" for="filterSortRadio3">Blue</label>-->
<!--          </div>-->

<!--          <div class="form-check">-->
<!--            <input class="form-check-input" type="radio" name="filterSortRadioOptions" id="filterSortRadio4" value="gray">-->
<!--            <label class="form-check-label" for="filterSortRadio4">Gray</label>-->
<!--          </div>-->
<!--        </div>-->

<!--        <div class="col-md-6" data-mdb-filter="sale">-->
<!--          <span class="fa-lg mb-5">Filter: Sale</span>-->

<!--          <div class="form-check mt-3">-->
<!--            <input class="form-check-input" type="radio" name="filterSortRadioOptions2" id="filterSortRadio5" value="yes">-->
<!--            <label class="form-check-label" for="filterSortRadio5">Yes</label>-->
<!--          </div>-->

<!--          <div class="form-check">-->
<!--            <input class="form-check-input" type="radio" name="filterSortRadioOptions2" id="filterSortRadio6" value="no">-->
<!--            <label class="form-check-label" for="filterSortRadio6">No</label>-->
<!--          </div>-->

<!--          <button type="button" class="btn btn-primary mt-3" id="filterSortReset">-->
<!--            Clear all filters-->
<!--          </button>-->
<!--        </div>-->

<!--        <div class="col-md-8 my-5">-->
<!--          <div id="select-wrapper-filter-sort-select" class="select-wrapper">-->
<!--            <div class="form-outline">-->
<!--              <input class="form-control select-input" type="text" role="listbox" aria-multiselectable="false" aria-disabled="false" aria-haspopup="true" aria-expanded="false" readonly="true">-->
<!--              <label class="form-label select-label active" style="margin-left: 0px;">Sort</label>-->
<!--              <span class="select-arrow"></span>-->
<!--              <div class="form-notch">-->
<!--                <div class="form-notch-leading" style="width: 9px;"></div>-->
<!--                <div class="form-notch-middle" style="width: 32px;"></div><div class="form-notch-trailing"></div></div><div class="form-label select-fake-value active">Choose category</div></div><select class="select select-initialized" id="filter-sort-select">-->
<!--            <option value="" disabled="" selected="">Choose category</option>-->
<!--            <option value="1">Product name ascending</option>-->
<!--            <option value="2">Product name descending</option>-->
<!--            <option value="3">Highest price</option>-->
<!--            <option value="4">Lowest price</option>-->
<!--          </select></div>-->

<!--        </div>-->
<!--      </div>-->
    <table class="table">
      <thead>
          <tr>
            <th>Предмет</th>
            <th>Оценки</th>
            <th>Средний балл</th>
          </tr>
      </thead>
      <tbody>
        <tr v-for="(data, studyGroupSubjectId) in marksTable" :key="studyGroupSubjectId">
          <td>{{data.name}}</td>
          <td>
            <div class="row">
              <div class="col" v-for="mark of data.marks" :key="mark">
                <p>{{mark}}</p>
              </div>
            </div>
          </td>
          <td>{{countAverage(data.marks)}}</td>
        </tr>
      </tbody>
    </table>

    </section>
</div>
</template>

<style scoped>

</style>
