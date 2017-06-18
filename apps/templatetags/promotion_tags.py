from django.template import Library, RequestContext
from django.template.loader import select_template
from oscar.templatetags.promotion_tags import PromotionNode as CorePromotion

register = Library()

class PromotionNode (CorePromotion):
    def render(self, context):
        promotion = self.promotion_var.resolve(context)
        template = select_template([promotion.template_name(),
                                    'promotions/default.html'])
        request = context['request']
        args = {'promotion': promotion}
        args.update(**promotion.template_context(request=context['request']))
        args.update({'request': request})
        ctx = RequestContext(context['request'], args)
        return template.render(ctx)

def get_promotion_html(parser, token):
    _, promotion = token.split_contents()
    return PromotionNode(promotion)


register.tag('render_promotion', get_promotion_html)