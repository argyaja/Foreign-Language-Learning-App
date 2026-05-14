from django.shortcuts import render

from app.forms.QuestionForm import QuestionForm

def faq_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'faq.html', {
                'form': QuestionForm(),
                # 'faqs': get_faqs_from_database(),  # Assuming you have a function to fetch FAQs from the database
                'success_message': 'Berhasil menambahkan pertanyaan!',
            })
        else:
            return render(request, 'faq.html', {
                'form': form,
                # 'faqs': get_faqs_from_database(),  # Assuming you have a function to fetch FAQs from the database
                'error_message': 'Kesalahan saat pengisian, pastikan Nama, Email, dan Pertanyaan terisi dengan benar',
            })
    else:
        form = QuestionForm()

    context = {
        'form': form,
        # 'faqs': get_faqs_from_database(),  # Assuming you have a function to fetch FAQs from the database
    }
    return render(request, 'faq.html', context)