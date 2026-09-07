"""Self-marking multiple choice for the revision.

Put this file beside the summary notebooks. Each notebook does:

    from mcq import check_answer, show_answer

then, for each question:

    my_answer = 'c'
    check_answer('w1a_m1', my_answer)

The answers and explanations below are encoded. That is so opening this file, or
scrolling past it, does not spoil the questions. It is a speed bump, not
security: anything sent to a browser can be read by whoever is using it, and a
determined student can decode this in one line. Nothing here is assessed, so
that is fine. The point is that you attempt each question first.
"""

import base64
import hashlib
import textwrap


def _h(s):
    return hashlib.sha256(str(s).strip().lower().encode()).hexdigest()[:12]


def _d(t):
    return base64.b64decode(t).decode()


def check_answer(qid, answer):
    """Say whether an answer is right.

    Wrong gets a nudge, so you can try again. Right gets the reason, including
    why the tempting option tempts.
    """
    if qid not in _KEY:
        print("There is no question called", repr(qid))
        print("Check the id in the cell above.")
        return
    want, why, nudge = _KEY[qid]
    if _h(answer) == want:
        print("Correct.\n")
        print(textwrap.fill(_d(why), 76))
    else:
        print("Not correct.\n")
        print(textwrap.fill(_d(nudge), 76))
        print("\nTry again, or run show_answer(" + repr(qid) + ") to see why.")


def show_answer(qid):
    """Print the explanation without answering."""
    if qid not in _KEY:
        print("There is no question called", repr(qid))
        return
    print(textwrap.fill(_d(_KEY[qid][1]), 76))


def questions(prefix=""):
    """List the question ids, optionally for one notebook."""
    return sorted(q for q in _KEY if q.startswith(prefix))


_KEY = {
    'w1a_m1': ('2e7d2c03a950',
     'UG9zaXRpb25zIHN0YXJ0IGF0IHplcm8sIHNvIGl0ZW0oMikgaXMgdGhlIHRoaXJkIGVsZW1lbnQsIDYuIE9wdGlvbiBiIGlzIHRoZSBhbnN3ZXIgeW91IGdldCBpZiB5b3UgY291bnQgZnJvbSBvbmUsIHdoaWNoIGlzIHRoZSBjb21tb25lc3Qgc2xpcCBpbiB0aGlzIGNvdXJzZS4=',
     'Q291bnQgdGhlIHBvc2l0aW9ucyBvdXQgbG91ZCwgc3RhcnRpbmcgYXQgemVyby4='),
    'w1a_m2': ('ca978112ca1b',
     'SXQgc2NhbGVzIGV2ZXJ5IGVsZW1lbnQsIGdpdmluZyBhcnJheShbMywgNiwgOV0pLiBPcHRpb24gYiBpcyB3aGF0ICogZG9lcyB0byBhIHN0cmluZywgYW5kIHRoYXQgaXMgd2h5IGl0IHRlbXB0cyBwZW9wbGU6IGFuIG9wZXJhdG9yIGJlaGF2ZXMgZGlmZmVyZW50bHkgZGVwZW5kaW5nIG9uIHRoZSB0eXBlIG9mIHRoZSB2YWx1ZXMgZWl0aGVyIHNpZGUgb2YgaXQu',
     'V2hhdCB0eXBlIGlzIHRoaXM/IFRoZSBhbnN3ZXIgd291bGQgYmUgZGlmZmVyZW50IGZvciB0ZXh0Lg=='),
    'w1a_m3': ('3e23e8160039',
     'U3RhcnQgYXQgMiwgc3RlcCBieSAzLCBhbmQgc3RvcCBiZWZvcmUgMTEsIHdoaWNoIGdpdmVzIDIsIDUgYW5kIDguIE9wdGlvbiBhIGlzIHRoZSBhbnN3ZXIgaWYgeW91IHJlYWQgc3RvcCBhcyBpbmNsdWRlZC4gSXQgbmV2ZXIgaXMu',
     'V3JpdGUgdGhlIHZhbHVlcyBvdXQgb25lIGF0IGEgdGltZS4gV2hlcmUgZG9lcyBpdCBoYXZlIHRvIGhhbHQ/'),
    'w1a_m4': ('2e7d2c03a950',
     'RWxlbWVudC1ieS1lbGVtZW50IGFyaXRobWV0aWMgcGFpcnMgdmFsdWVzIGJ5IHBvc2l0aW9uLCBzbyBib3RoIGFycmF5cyBtdXN0IGJlIHRoZSBzYW1lIGxlbmd0aC4gRm91ciBhZ2FpbnN0IHR3byBjYW5ub3QgcGFpciwgYW5kIG51bXB5IHJlcG9ydHMgaXQgYXMgc2hhcGVzICg0LCkgYW5kICgyLCkuIENoZWNraW5nIGxlbiBvbiBib3RoIGNvbmZpcm1zIGl0IGZhc3Rlc3Qu',
     'UmVhZCB0aGUgZXJyb3IgbWVzc2FnZS4gSXQgbWVudGlvbnMgc2hhcGVzLiBXaGF0IGlzIGEgc2hhcGUgaGVyZT8='),
    'w1a_m5': ('2e7d2c03a950',
     'c3VtIGNvbGxhcHNlcyB0aGUgd2hvbGUgYXJyYXkgdG8gb25lIHZhbHVlLiBUaGUgZmlyc3QgdHdvIGFwcGx5IHRvIGV2ZXJ5IGVsZW1lbnQgYW5kIGhhbmQgYmFjayBhbiBhcnJheSBvZiB0aGUgc2FtZSBsZW5ndGgsIGFuZCBhcmFuZ2UgYnVpbGRzIGEgbmV3IGFycmF5LiBLbm93aW5nIHdoaWNoIHNoYXBlIHlvdSBhcmUgaG9sZGluZyBpcyB3aGF0IHRlbGxzIHlvdSB0aGUgbmV4dCBzdGVwIGlzIGFsbG93ZWQu',
     'VHdvIGRpZmZlcmVudCBzaGFwZXMgb2YgcmVzdWx0IGhlcmUuIFdoaWNoIG9uZSBsb3NlcyB0aGUgbGVuZ3RoPw=='),
    'w1p_m1': ('3e23e8160039',
     'T25seSB0aGUgbGFzdCBsaW5lIG9mIGEgY2VsbCBpcyBkaXNwbGF5ZWQuIEJvdGggc3VtcyBhcmUgd29ya2VkIG91dDsgdGhlIGZpcnN0IGlzIHNpbXBseSBub3Qgc2hvd24uIE5vdGhpbmcgaXMgbG9zdCBpZiB5b3UgYXNzaWduIGl0IHRvIGEgbmFtZS4=',
     'SG93IG1hbnkgdmFsdWVzIGRvZXMgYSBjZWxsIHNob3cgeW91LCBob3dldmVyIG1hbnkgaXQgY29tcHV0ZXM/'),
    'w1p_m2': ('2e7d2c03a950',
     'aW50KC0xLjYpIGlzIC0xLiBpbnQgdHJ1bmNhdGVzIHRvd2FyZHMgemVybywgd2hpY2ggaXMgbm90IHRoZSBzYW1lIGFzIHJvdW5kaW5nIGRvd24uIE9wdGlvbiBiLCAtMiwgaXMgd2hhdCB5b3UgZ2V0IGZyb20gcm91bmRpbmcgZG93biwgYW5kIHRoYXQgaXMgdGhlIHRyYXAu',
     'VHJ1bmNhdGluZyB0b3dhcmRzIHplcm8gYW5kIHJvdW5kaW5nIGRvd24gYWdyZWUgZm9yIHBvc2l0aXZlIG51bWJlcnMuIFRoZXkgZG8gbm90IGFncmVlIGhlcmUu'),
    'w1p_m3': ('18ac3e7343f0',
     'aW50KCc3Ljk5JykgZmFpbHMsIGJlY2F1c2UgaW50IGNhbiBvbmx5IHJlYWQgYSB3aG9sZS1udW1iZXIgc3RyaW5nLiBpbnQoZmxvYXQoJzcuOTknKSkgd29ya3MgYW5kIGdpdmVzIDc6IHRoZSB0ZXh0IGJlY29tZXMgYSBudW1iZXIgZmlyc3QsIHRoZW4gYSB3aG9sZSBudW1iZXIu',
     'V2hhdCBkb2VzIGludCBhY2NlcHQgYXMgdGV4dD8gVHJ5IGVhY2ggb25lIGluIGEgY2VsbC4='),
    'w1p_m4': ('ca978112ca1b',
     'RGl2aXNpb24gYWx3YXlzIGdpdmVzIGEgZmxvYXQsIGV2ZW4gd2hlbiBpdCBkaXZpZGVzIGV2ZW5seSwgc28gNDA0OCAvIDIgaXMgMjAyNC4wIGFuZCBpdHMgdHlwZSBpcyBmbG9hdC4gVGhhdCBzdXJwcmlzZXMgcGVvcGxlLCB3aGljaCBpcyB3aHkgaXQgaXMgd29ydGggcmVtZW1iZXJpbmcu',
     'RG9lcyBpdCBtYXR0ZXIgd2hldGhlciB0aGUgYW5zd2VyIGNvbWVzIG91dCB3aG9sZT8='),
    'w1p_m5': ('3e23e8160039',
     'dG90YWwga2VlcHMgdGhlIHZhbHVlIHdvcmtlZCBvdXQgd2hlbiB0aGUgbGluZSByYW4uIENoYW5naW5nIGEgYWZ0ZXJ3YXJkcyBkb2VzIG5vdCByZWFjaCBiYWNrIGFuZCBjaGFuZ2UgdG90YWwuIFRoaXMgaXMgdGhlIGlkZWEgdGhhdCBtYWtlcyBhIG5vdGVib29rIGJlaGF2ZSBwcmVkaWN0YWJseS4=',
     'SXMgYSBuYW1lIGEgc3RvcmVkIGFuc3dlciwgb3IgYSBsaXZlIGZvcm11bGE/'),
    'w1t_m1': ('3e23e8160039',
     'c2VsZWN0IGdpdmVzIGJhY2sgYSB0YWJsZSwgZXZlbiBmb3Igb25lIGNvbHVtbi4gY29sdW1uIGdpdmVzIGJhY2sgYW4gYXJyYXkuIElmIGEgZnVuY3Rpb24gY29tcGxhaW5zIGFib3V0IHRoZSB0eXBlIGl0IHdhcyBoYW5kZWQsIHRoaXMgaXMgdGhlIGZpcnN0IHRoaW5nIHRvIGNoZWNrLg==',
     'T25lIG9mIHRoZW0gY2FuIGJlIHBhc3NlZCB0byBucC5hdmVyYWdlLiBXaGljaD8='),
    'w1t_m2': ('2e7d2c03a950',
     'VGhlIHZhbHVlcyBhcmUgc3RvcmVkIHdpdGggYSBjb3VudHJ5LWNvZGUgcHJlZml4LCBzbyBub3RoaW5nIG1hdGNoZXMgdGhlIGJhcmUgd29yZC4gWW91IGdldCBhbiBlbXB0eSB0YWJsZSBhbmQgbm8gZXJyb3IsIHdoaWNoIGlzIHRoZSBtb3N0IGRhbmdlcm91cyBraW5kIG9mIHdyb25nIGFuc3dlci4gTG9vayBhdCB0aGUgYWN0dWFsIHZhbHVlcyBmaXJzdC4=',
     'Tm90aGluZyBlcnJvcmVkLiBTbyB3aGF0IGRpZCBQeXRob24gdGhpbmsgeW91IGFza2VkIGZvcj8='),
    'w1t_m3': ('ca978112ca1b',
     'VGhlIGZpcnN0IGZhaWxzLiBkcm9wIHJlbW92ZXMgdGhlIGNvbHVtbiB0aGF0IHdoZXJlIHRoZW4gdHJpZXMgdG8gZmlsdGVyIG9uLiBGaWx0ZXIgZmlyc3QsIHRoZW4gZHJvcC4=',
     'UmVhZCB0aGVtIGxlZnQgdG8gcmlnaHQuIFdoYXQgZG9lcyB0aGUgc2Vjb25kIHN0ZXAgc3RpbGwgbmVlZD8='),
    'w1t_m4': ('18ac3e7343f0',
     'bnVtX3Jvd3MgaXMgYW4gYXR0cmlidXRlLCBub3QgYSBtZXRob2QsIHNvIGl0IHRha2VzIG5vIGJyYWNrZXRzLiBBZGRpbmcgdGhlbSB0cmllcyB0byBjYWxsIGFuIGludGVnZXIsIHdoaWNoIGZhaWxzLg==',
     'Q29tcGFyZSBpdCB3aXRoIHNob3coNSksIHdoaWNoIGRvZXMgdGFrZSBicmFja2V0cy4gV2hhdCBpcyB0aGUgZGlmZmVyZW5jZSBiZXR3ZWVuIHRoZSB0d28/'),
    'w1t_m5': ('3e23e8160039',
     'Tm90aGluZyBpcyBicm9rZW4uIGRyb3AgcmV0dXJucyBhIG5ldyB0YWJsZSBhbmQgbGVhdmVzIHRoZSBvcmlnaW5hbCBhbG9uZSwgd2hpY2ggaXMgdHJ1ZSBvZiBuZWFybHkgZXZlcnkgdGFibGUgbWV0aG9kLiBJZiB5b3Ugd2FudCB0byBrZWVwIHRoZSByZXN1bHQsIGFzc2lnbiBpdCB0byBhIG5hbWUu',
     'RGlkIHlvdSBhc3NpZ24gdGhlIHJlc3VsdCB0byBhbnl0aGluZz8='),
    'w2_m1': ('2e7d2c03a950',
     'SXQgYmVjb21lcyBQcmljZSBhdmVyYWdlLiBncm91cCB3aXRoIGEgZnVuY3Rpb24gcmVuYW1lcyBldmVyeSBhZ2dyZWdhdGVkIGNvbHVtbiwgc28gdGhlIG9sZCBuYW1lIG5vIGxvbmdlciBleGlzdHMgYW5kIGFza2luZyBmb3IgaXQgcmFpc2VzIGFuIGVycm9yLiBQcmludCAubGFiZWxzIGFmdGVyIGFueSBncm91cGVkIGFnZ3JlZ2F0aW9uLg==',
     'UnVuIC5sYWJlbHMgb24gdGhlIHJlc3VsdCBhbmQgbG9vay4='),
    'w2_m2': ('3e23e8160039',
     'UGFzcyB0aGUgZnVuY3Rpb24sIGRvIG5vdCBjYWxsIGl0LiBUaGUgYnJhY2tldHMgaW4gYXBwbHkoZigpLCBjb2wpIGNhbGwgZiBpbW1lZGlhdGVseSwgYmVmb3JlIGFwcGx5IGV2ZXIgc2VlcyBpdCwgc28gUHl0aG9uIGNvbXBsYWlucyBhYm91dCBtaXNzaW5nIGFyZ3VtZW50cy4gYXBwbHkgZG9lcyB0aGUgY2FsbGluZywgb25jZSBwZXIgcm93Lg==',
     'V2hvIGlzIHN1cHBvc2VkIHRvIGNhbGwgdGhlIGZ1bmN0aW9uLCB5b3Ugb3IgYXBwbHk/'),
    'w2_m3': ('18ac3e7343f0',
     'SXQgaXMgdGhlIGFyZWEgb2YgYSBiYXIgdGhhdCBnaXZlcyB0aGUgcHJvcG9ydGlvbiwgbm90IGl0cyBoZWlnaHQuIFRoZSBzZWNvbmQgYmFyIGlzIGhhbGYgdGhlIGhlaWdodCBidXQgZm91ciB0aW1lcyB0aGUgd2lkdGgsIHNvIGl0IGhvbGRzIHR3aWNlIGFzIG11Y2guIFdpdGggZXF1YWwtd2lkdGggYmlucyB5b3UgY291bGQgY29tcGFyZSBoZWlnaHRzIHNhZmVseS4=',
     'Q2hlY2sgdGhlIHdpZHRocyBiZWZvcmUgeW91IGNvbXBhcmUgYW55dGhpbmcu'),
    'w2_m4': ('ca978112ca1b',
     'am9pbiBrZWVwcyBvbmx5IHJvd3Mgd2hvc2Uga2V5IGFwcGVhcnMgaW4gYm90aCB0YWJsZXMsIHNvIHVubWF0Y2hlZCByb3dzIGRpc2FwcGVhciB3aXRoIG5vIGVycm9yIGFuZCBubyB3YXJuaW5nLiBDb21wYXJpbmcgbnVtX3Jvd3MgYmVmb3JlIGFuZCBhZnRlciBpcyB0aGUgb25seSBjaGVjayB5b3UgZ2V0Lg==',
     'V2hhdCBoYXBwZW5zIHRvIGEgcm93IGluIG9uZSB0YWJsZSB3aXRoIG5vIHBhcnRuZXIgaW4gdGhlIG90aGVyPw=='),
    'w2_m5': ('2e7d2c03a950',
     'QSBmdW5jdGlvbiB3aXRoIG5vIHJldHVybiBoYW5kcyBiYWNrIE5vbmUuIEl0IG1heSBwcmludCBzb21ldGhpbmcgb24gdGhlIHdheSwgYnV0IHByaW50aW5nIGFuZCByZXR1cm5pbmcgYXJlIGRpZmZlcmVudCB0aGluZ3MsIGFuZCBvbmx5IHRoZSByZXR1cm5lZCB2YWx1ZSBjYW4gYmUgc3RvcmVkIG9yIHVzZWQu',
     'UHJpbnRpbmcgcHV0cyBzb21ldGhpbmcgb24gdGhlIHNjcmVlbi4gV2hhdCBkb2VzIGl0IGhhbmQgYmFjaz8='),
    'w2b_m1': ('2e7d2c03a950',
     'OTk5IGlzIGEgc2VudGluZWw6IGEgY29kZSBzdGFuZGluZyBmb3Igc29tZXRoaW5nIG90aGVyIHRoYW4gYSBtZWFzdXJlbWVudCwgaGVyZSB0aGUgdG90YWwgYWNyb3NzIGFsbCBhZ2VzLiBBdmVyYWdpbmcgd2l0aCBpdCBpbiBwdWxscyB0aGUgYW5zd2VyIHVwd2FyZHMgYnkgYW4gYXJiaXRyYXJ5IGFtb3VudC4gU29ydCBlYWNoIG51bWVyaWMgY29sdW1uIGFuZCBsb29rIGF0IGJvdGggZW5kcyBiZWZvcmUgY29tcHV0aW5nIGFueXRoaW5nLg==',
     'SXMgYW55b25lIDk5OSB5ZWFycyBvbGQ/IFNvIHdoYXQgaXMgdGhhdCByb3c/'),
    'w2b_m2': ('3e23e8160039',
     'cmVsYWJlbGVkIHJldHVybnMgYSBuZXcgdGFibGUgYW5kIGxlYXZlcyB0aGUgb3JpZ2luYWwgYWxvbmUuIHJlbGFiZWwgY2hhbmdlcyB0aGUgb3JpZ2luYWwgaW4gcGxhY2UuIE1vc3QgdGFibGUgbWV0aG9kcyBiZWhhdmUgbGlrZSB0aGUgZmlyc3Q7IHJlbGFiZWwgaXMgb25lIG9mIHRoZSBmZXcgdGhhdCBkb2VzIG5vdC4=',
     'T25lIG9mIHRoZW0gY2hhbmdlcyB0aGUgdGFibGUgeW91IGNhbGxlZCBpdCBvbi4gV2hpY2g/'),
    'w2b_m3': ('ca978112ca1b',
     'Q29tcGFyZSBudW1fcm93cyBiZWZvcmUgYW5kIGFmdGVyLiBJZiB5b3UgZXhwZWN0ZWQgdG8gZHJvcCBhIGhhbmRmdWwgb2Ygcm93cyBhbmQgbG9zdCBoYWxmIHRoZSB0YWJsZSwgdGhlIGNvbmRpdGlvbiBpcyB3cm9uZy4gSXQgY29zdHMgb25lIGxpbmUgYW5kIGNhdGNoZXMgdGhlIGNvbW1vbmVzdCBmaWx0ZXJpbmcgbWlzdGFrZS4=',
     'WW91IG5lZWQgYSBudW1iZXIgeW91IGNhbiBjb21wYXJlIGFnYWluc3Qgc29tZXRoaW5nLg=='),
    'w2b_m4': ('18ac3e7343f0',
     'cmVsYWJlbGxlZCB3aXRoIHR3byBsJ3MgaXMgbm90IGEgbWV0aG9kIGF0IGFsbCBhbmQgcmFpc2VzIGFuIEF0dHJpYnV0ZUVycm9yLiBUaGUgZGF0YXNjaWVuY2UgbGlicmFyeSB1c2VzIHRoZSBBbWVyaWNhbiBzcGVsbGluZywgd2hpY2ggaXMgb25lIG9mIHRoZSBmZXcgcGxhY2VzIGluIHRoaXMgY291cnNlIHdoZXJlIGl0IGlzIHRoZSBjb3JyZWN0IG9uZS4=',
     'Q291bnQgdGhlIGwncy4='),
    'w2b_m5': ('3e23e8160039',
     'c2hvdyg1KSByZXZlYWxzIHRoZSBjb2x1bW4gbmFtZXMsIHRoZSB0eXBlcyBvZiB0aGUgdmFsdWVzLCBhbmQgd2hldGhlciB0aGUgZmlsZSBoYXMgdG90YWxzIG9yIGZvb3Rub3RlcyBtaXhlZCBpbiB3aXRoIHRoZSBkYXRhLiBudW1fcm93cyBvbmx5IHRlbGxzIHlvdSBob3cgbWFueSByb3dzIHRoZXJlIGFyZSwgbm90IHdoZXRoZXIgdGhleSBhcmUgb2JzZXJ2YXRpb25zLg==',
     'T25lIG9mIHRoZW0gdGVsbHMgeW91IHdoYXQgaXMgaW4gdGhlIHRhYmxlLCBub3QganVzdCBob3cgYmlnIGl0IGlzLg=='),
    'w3_m1': ('3e23e8160039',
     'bnAuYXBwZW5kIHJldHVybnMgYSBuZXcgYXJyYXkgYW5kIGRvZXMgbm90IGNoYW5nZSB0aGUgb25lIGl0IHdhcyBnaXZlbi4gV2l0aG91dCByZXN1bHRzID0gaW4gZnJvbnQsIHRoZSBuZXcgYXJyYXkgaXMgYnVpbHQgYW5kIHRocm93biBhd2F5LCBzbyByZXN1bHRzIHN0YXlzIGVtcHR5LiBOb3RoaW5nIGVycm9ycyBhbmQgbm90aGluZyB3YXJucyB5b3Uu',
     'V2hhdCBkb2VzIG5wLmFwcGVuZCBoYW5kIGJhY2ssIGFuZCB3aGVyZSBkb2VzIGl0IGdvPw=='),
    'w3_m2': ('ca978112ca1b',
     'QW4gYXJyYXkgb2YgMTAwIGJvb2xlYW5zLCBvbmUgcGVyIGVsZW1lbnQuIEEgY29tcGFyaXNvbiBvbiBhbiBhcnJheSBpcyBhbnN3ZXJlZCBlbGVtZW50IGJ5IGVsZW1lbnQuIElmIHlvdSBleHBlY3RlZCBvbmUgYW5zd2VyLCB5b3UgbWF5IGhhdmUgbWVhbnQgbnAuYWxsIG9yIG5wLmFueS4=',
     'SG93IG1hbnkgcXVlc3Rpb25zIGRpZCB5b3UganVzdCBhc2s/'),
    'w3_m3': ('2e7d2c03a950',
     'bnAuYXZlcmFnZSBnaXZlcyB0aGUgcHJvcG9ydGlvbiwgbnAuY291bnRfbm9uemVybyBnaXZlcyB0aGUgY291bnQuIFRydWUgY291bnRzIGFzIDEgYW5kIEZhbHNlIGFzIDAsIHNvIHRoZSBtZWFuIG9mIGFuIGFycmF5IG9mIGJvb2xlYW5zIGlzIHRoZSBmcmFjdGlvbiB0aGF0IGFyZSBUcnVlLg==',
     'T25lIG9mIHRoZW0gY2FuIG5ldmVyIGJlIGJpZ2dlciB0aGFuIDEu'),
    'w3_m4': ('ca978112ca1b',
     'VGhlIGZpcnN0IHRydWUgY29uZGl0aW9uIHdpbnMgYW5kIHRoZSByZXN0IGFyZSBuZXZlciB0ZXN0ZWQuIFRoYXQgaXMgd2h5IG9yZGVyIG1hdHRlcnM6IGEgYnJvYWQgY29uZGl0aW9uIHBsYWNlZCBmaXJzdCBzd2FsbG93cyBldmVyeSBjYXNlIGEgbmFycm93ZXIgb25lIGJlbG93IGl0IHdhcyBtZWFudCB0byBjYXRjaC4=',
     'RG9lcyBQeXRob24ga2VlcCBjaGVja2luZyBhZnRlciBpdCBmaW5kcyBhIG1hdGNoPw=='),
    'w3_m5': ('18ac3e7343f0',
     'PSBhc3NpZ25zIGFuZCByZXR1cm5zIG5vdGhpbmc7ID09IGFza3MgYSBxdWVzdGlvbiBhbmQgZ2l2ZXMgYmFjayBUcnVlIG9yIEZhbHNlLiBPbmx5IHRoZSBhc3NpZ25tZW50IGNoYW5nZXMgYW55dGhpbmcsIGFuZCBvbmx5IHRoZSBjb21wYXJpc29uIHByb2R1Y2VzIGEgdmFsdWUgeW91IGNhbiB1c2Uu',
     'T25lIG9mIHRoZW0gY2hhbmdlcyB0aGUgd29ybGQuIFRoZSBvdGhlciBhc2tzIGFib3V0IGl0Lg=='),
    'w3b_m1': ('3e23e8160039',
     'c2FtcGxlIGRyYXdzIHdpdGggcmVwbGFjZW1lbnQgYnkgZGVmYXVsdCwgc28gc29tZSByb3dzIGFwcGVhciBtb3JlIHRoYW4gb25jZSBhbmQgb3RoZXJzIG5vdCBhdCBhbGwuIEZvciBhIHNodWZmbGUgb2YgdGhlIG9yaWdpbmFsIHJvd3MgeW91IG5lZWQgd2l0aF9yZXBsYWNlbWVudD1GYWxzZS4=',
     'V2hhdCBpcyB0aGUgZGVmYXVsdD8gSXQgaXMgbm90IHRoZSBjYXV0aW91cyBvbmUu'),
    'w3b_m2': ('2e7d2c03a950',
     'c2FtcGxlX3Byb3BvcnRpb25zIHRha2VzIHByb3BvcnRpb25zIHRoYXQgc3VtIHRvIDEsIG5vdCBjb3VudHMuIFdyaXR0ZW4gY29ycmVjdGx5IGl0IGlzIHNhbXBsZV9wcm9wb3J0aW9ucygyMDAsIG1ha2VfYXJyYXkoMC41LCAwLjMsIDAuMikpLg==',
     'QWRkIHRoZSB0aHJlZSBudW1iZXJzIHVwLiBXaGF0IHNob3VsZCB0aGV5IGNvbWUgdG8/'),
    'w3b_m3': ('ca978112ca1b',
     'QWJvdXQgMTA0LiBUaGUgb3V0cHV0IGlzIHByb3BvcnRpb25zLCBub3QgY291bnRzLCBzbyBtdWx0aXBseSBieSB0aGUgc2FtcGxlIHNpemUuIEZvcmdldHRpbmcgdGhpcyBpcyB0aGUgY29tbW9uZXN0IGVycm9yIHdpdGggdGhpcyBmdW5jdGlvbiwgYW5kIGl0IGdvZXMgaW4gYm90aCBkaXJlY3Rpb25zOiBwcm9wb3J0aW9ucyBpbiwgcHJvcG9ydGlvbnMgb3V0Lg==',
     'MC41MiBvZiBob3cgbWFueT8='),
    'w3b_m4': ('18ac3e7343f0',
     'QSBsYXJnZXIgYmlhc2VkIHNhbXBsZSBpcyBzdGlsbCBiaWFzZWQuIFNpemUgcmVkdWNlcyB0aGUgZWZmZWN0IG9mIGNoYW5jZSwgbm90IHRoZSBlZmZlY3Qgb2YgYSBtZXRob2QgdGhhdCBzeXN0ZW1hdGljYWxseSBmYXZvdXJzIHNvbWUgcm93cyBvdmVyIG90aGVycy4gT25seSBhIGJldHRlciBzYW1wbGluZyBtZXRob2QgZml4ZXMgYmlhcy4=',
     'RG9lcyB0YWtpbmcgbW9yZSBvZiBzb21ldGhpbmcgY3Jvb2tlZCBtYWtlIGl0IHN0cmFpZ2h0Pw=='),
    'w3b_m5': ('3e23e8160039',
     'SXQgaXMgdGhlIHByb3BvcnRpb24gb2Ygc2ltdWxhdGVkIHJlc3VsdHMgYXQgbGVhc3QgYXMgZXh0cmVtZSBhcyB0aGUgb2JzZXJ2ZWQgb25lLCBpZiB0aGUgbW9kZWwgd2VyZSB0cnVlLiBJdCBpcyBub3QgdGhlIHByb2JhYmlsaXR5IHRoYXQgdGhlIG1vZGVsIGlzIGZhbHNlLCBhbmQgbm90IHRoZSBwcm9iYWJpbGl0eSB0aGF0IHlvdXIgcmVzdWx0IHdhcyBsdWNrLg==',
     'SXQgaXMgYSBwcm9wb3J0aW9uIG9mIHNvbWV0aGluZyB5b3Ugc2ltdWxhdGVkLiBPZiB3aGF0LCBleGFjdGx5Pw=='),
    'w4_m1': ('2e7d2c03a950',
     'RmFsc2Ugc29ydHMgYmVmb3JlIFRydWUsIHNvIGl0IGlzIGl0ZW0oMCkuIGdyb3VwIHNvcnRzIGl0cyByb3dzLCBhbmQgYSBkaWZmZXJlbmNlIGNvbXB1dGVkIGFzIGl0ZW0oMSkgLSBpdGVtKDApIGlzIHRoZXJlZm9yZSB0cnVlIG1pbnVzIGZhbHNlLiBOZXZlciBhc3N1bWUgdGhlIG9yaWdpbmFsIG9yZGVyIHN1cnZpdmVkLg==',
     'V2hhdCBvcmRlciBkb2VzIGdyb3VwIHB1dCBpdHMgcm93cyBpbj8='),
    'w4_m2': ('ca978112ca1b',
     'U2h1ZmZsaW5nIGJyZWFrcyBhbnkgcmVhbCBsaW5rIGJldHdlZW4gbGFiZWwgYW5kIHZhbHVlIHdoaWxlIGtlZXBpbmcgYm90aCBncm91cCBzaXplcyB0aGUgc2FtZS4gU28gYW55IGRpZmZlcmVuY2UgdGhhdCBzdXJ2aXZlcyBpcyBjaGFuY2UgYWxvbmUsIHdoaWNoIGlzIGV4YWN0bHkgd2hhdCB0aGUgbnVsbCBoeXBvdGhlc2lzIGNsYWltcyB0aGUgcmVhbCBkaWZmZXJlbmNlIGlzLg==',
     'V2hhdCBpcyB0aGUgbnVsbCBoeXBvdGhlc2lzIGFjdHVhbGx5IGNsYWltaW5nPw=='),
    'w4_m3': ('18ac3e7343f0',
     'U2h1ZmZsZSB3aXRob3V0IHJlcGxhY2VtZW50LiBXaXRoIHJlcGxhY2VtZW50IHRoZSBncm91cCBzaXplcyBjaGFuZ2UsIGFuZCB5b3Ugd291bGQgYmUgdGVzdGluZyBzb21ldGhpbmcgb3RoZXIgdGhhbiB0aGUgcXVlc3Rpb24geW91IGFza2VkLg==',
     'V2hhdCBoYXMgdG8gc3RheSB0aGUgc2FtZSBmb3IgdGhlIGNvbXBhcmlzb24gdG8gYmUgZmFpcj8='),
    'w4_m4': ('3e23e8160039',
     'SXQgaXMgdGhlIHByb3BvcnRpb24gb2Ygc2ltdWxhdGVkIGRpZmZlcmVuY2VzIGF0IGxlYXN0IGFzIGV4dHJlbWUgYXMgdGhlIG9ic2VydmVkIG9uZSwgYXNzdW1pbmcgdGhlIG51bGwuIEl0IGlzIG5vdCB0aGUgcHJvYmFiaWxpdHkgdGhhdCB0aGUgbnVsbCBpcyB0cnVlLCBhbmQgbm90IHRoZSBwcm9iYWJpbGl0eSB5b3VyIHJlc3VsdCB3YXMgbHVjay4=',
     'V2hpY2ggd2F5IHJvdW5kIGlzIHRoZSBjb25kaXRpb25hbD8gR2l2ZW4gd2hhdCwgZXhhY3RseT8='),
    'w4_m5': ('2e7d2c03a950',
     'SXQgcnVsZXMgb3V0IGNoYW5jZSwgbm90IGEgY29uZm91bmRlci4gQSB2YXJpYWJsZSB0aGF0IGRpZmZlcnMgYmV0d2VlbiB0aGUgZ3JvdXBzIGNhbiBleHBsYWluIHRoZSBvdXRjb21lLCBhbmQgbm8gYW1vdW50IG9mIHNodWZmbGluZyBkZXRlY3RzIHRoYXQuIE9ubHkgcmFuZG9tIGFzc2lnbm1lbnQgdG8gdGhlIGdyb3VwcyBzdXBwb3J0cyBhIGNhdXNhbCBjbGFpbS4=',
     'V2hhdCBoYXMgdGhlIHRlc3QgY29tcGFyZWQgdGhlIGRhdGEgYWdhaW5zdD8gT25seSBvbmUgYWx0ZXJuYXRpdmUu'),
    'w5_m1': ('2e7d2c03a950',
     'VGhlIHNhbWUgc2l6ZSBhcyB0aGUgb3JpZ2luYWwgc2FtcGxlLCBkcmF3biB3aXRoIHJlcGxhY2VtZW50LiBUaGUgYm9vdHN0cmFwIGltaXRhdGVzIGRyYXdpbmcgYSBmcmVzaCBzYW1wbGUgZnJvbSB0aGUgcG9wdWxhdGlvbiwgc28gaXQgbXVzdCBpbWl0YXRlIHRoZSBzYW1wbGUgc2l6ZSB0b28uIEEgc21hbGxlciByZXNhbXBsZSBvdmVyc3RhdGVzIHRoZSB2YXJpYWJpbGl0eS4=',
     'V2hhdCBpcyB0aGUgYm9vdHN0cmFwIHByZXRlbmRpbmcgdG8gZG8/'),
    'w5_m2': ('18ac3e7343f0',
     'V2l0aG91dCByZXBsYWNlbWVudCwgZXZlcnkgcmVzYW1wbGUgaXMganVzdCB0aGUgb3JpZ2luYWwgc2FtcGxlIHJlb3JkZXJlZCwgc28gZXZlcnkgcmVzYW1wbGVkIHN0YXRpc3RpYyBpcyBpZGVudGljYWwgYW5kIHRoZSBpbnRlcnZhbCBoYXMgemVybyB3aWR0aC4gUmVwbGFjZW1lbnQgaXMgd2hhdCBjcmVhdGVzIHRoZSB2YXJpYXRpb24geW91IGFyZSBtZWFzdXJpbmcu',
     'SWYgeW91IGRyYXcgYWxsIDQwMCByb3dzIHdpdGhvdXQgcmVwbGFjZW1lbnQsIHdoYXQgaGF2ZSB5b3UgZ290Pw=='),
    'w5_m3': ('3e23e8160039',
     'VGhlIDk1JSBkZXNjcmliZXMgdGhlIHByb2NlZHVyZS4gUmVwZWF0IHRoZSB3aG9sZSBidXNpbmVzcyBtYW55IHRpbWVzIGFuZCBhYm91dCA5NSBpbnRlcnZhbHMgaW4gMTAwIGNvdmVyIHRoZSB0cnV0aC4gVGhlIHRydWUgdmFsdWUgaXMgZml4ZWQ6IHRoaXMgcGFydGljdWxhciBpbnRlcnZhbCBlaXRoZXIgY29udGFpbnMgaXQgb3IgZG9lcyBub3QsIGFuZCB5b3UgY2Fubm90IHRlbGwgd2hpY2guIE9wdGlvbiBhIGlzIHRoZSBwaHJhc2luZyBtb3N0IHBlb3BsZSB3cml0ZSwgYW5kIGl0IGlzIHdyb25nLg==',
     'V2hpY2ggdGhpbmcgbW92ZXMgYmV0d2VlbiByZXBlYXRzLCB0aGUgcGFyYW1ldGVyIG9yIHRoZSBpbnRlcnZhbD8='),
    'w5_m4': ('ca978112ca1b',
     'QSBoaWdoZXIgY29uZmlkZW5jZSBsZXZlbCBuZWVkcyBhIHdpZGVyIGludGVydmFsLCBiZWNhdXNlIGl0IG11c3QgY2F0Y2ggbW9yZSBvZiB0aGUgYm9vdHN0cmFwIGRpc3RyaWJ1dGlvbi4gVG8gbmFycm93IGFuIGludGVydmFsIHlvdSBuZWVkIGEgbGFyZ2VyIHNhbXBsZSwgbm90IG1vcmUgY29uZmlkZW5jZS4=',
     'TW9yZSBjb25maWRlbnQgYWJvdXQgYSBjbGFpbSB1c3VhbGx5IG1lYW5zIGNsYWltaW5nIGxlc3MgcHJlY2lzZWx5Lg=='),
    'w5_m5': ('2e7d2c03a950',
     'TWVhbiAwIGFuZCBzdGFuZGFyZCBkZXZpYXRpb24gMSwgYWx3YXlzLCB3aGF0ZXZlciB5b3Ugc3RhcnRlZCB3aXRoLiBUaGF0IGlzIHdoYXQgbWFrZXMgdHdvIHF1YW50aXRpZXMgbWVhc3VyZWQgb24gY29tcGxldGVseSBkaWZmZXJlbnQgc2NhbGVzIGNvbXBhcmFibGUsIGFuZCBpdCBpcyB3aHkgdGhlIGNvcnJlbGF0aW9uIGNvZWZmaWNpZW50IHdvcmtzLg==',
     'U3VidHJhY3QgdGhlIG1lYW4sIHRoZW4gZGl2aWRlIGJ5IHRoZSBTRC4gV2hhdCBpcyBsZWZ0Pw=='),
    'w6_m1': ('18ac3e7343f0',
     'VGhlcmUgbWF5IGJlIGEgdmVyeSBzdHJvbmcgcmVsYXRpb25zaGlwLiByIG1lYXN1cmVzIG9ubHkgdGhlIGxpbmVhciBwYXJ0IG9mIGFuIGFzc29jaWF0aW9uLCBhbmQgYSBzeW1tZXRyaWMgY3VydmUgaGFzIGFsbW9zdCBub25lLiBBbHdheXMgbG9vayBhdCB0aGUgc2NhdHRlciBwbG90IGJlZm9yZSB0cnVzdGluZyByLg==',
     'V2hhdCB3b3JkIGlzIGRvaW5nIHRoZSB3b3JrIGluIHRoZSBwaHJhc2UgbGluZWFyIGFzc29jaWF0aW9uPw=='),
    'w6_m2': ('3e23e8160039',
     'UmVncmVzc2lvbiB0byB0aGUgbWVhbiwgYW5kIGl0IGhhcHBlbnMgd2hlbmV2ZXIgdGhlIHNpemUgb2YgciBpcyBsZXNzIHRoYW4gMS4gSW4gc3RhbmRhcmQgdW5pdHMgdGhlIHByZWRpY3RlZCB5IGlzIHIgdGltZXMgdGhlIHgsIHNvIGV2ZXJ5IHByZWRpY3Rpb24gc2l0cyBjbG9zZXIgdG8gYXZlcmFnZSB0aGFuIHRoZSB2YWx1ZSB0aGF0IHByb2R1Y2VkIGl0LiBJdCBpcyBhcml0aG1ldGljLCBub3QgYSBjbGFpbSBhYm91dCBwZW9wbGUu',
     'SW4gc3RhbmRhcmQgdW5pdHMsIHdoYXQgaXMgdGhlIHNsb3BlIG9mIHRoZSBsaW5lPw=='),
    'w6_m3': ('ca978112ca1b',
     'QSBmb3JtbGVzcyBob3Jpem9udGFsIGJhbmQuIEFueSBjdXJ2ZSBtZWFucyB0aGUgcmVsYXRpb25zaGlwIGJlbmRzIGFuZCBhIHN0cmFpZ2h0IGxpbmUgaXMgdGhlIHdyb25nIHNoYXBlLCBob3dldmVyIHJlc3BlY3RhYmxlIHIgbG9va2VkLiBUaGF0IGlzIHdoYXQgdGhlIHJlc2lkdWFsIHBsb3QgaXMgZm9yLCBhbmQgciB3b3VsZCBub3QgaGF2ZSB3YXJuZWQgeW91Lg==',
     'WW91IHdhbnQgdG8gc2VlIG5vdGhpbmcgYXQgYWxsLiBXaGF0IGRvZXMgbm90aGluZyBsb29rIGxpa2U/'),
    'w6_m4': ('2e7d2c03a950',
     'Tm90aGluZyBob2xkcyB0aGUgbGluZSB1cCBvdXQgdGhlcmUuIEl0IHdhcyBmaXR0ZWQgd2hlcmUgdGhlIGRhdGEgaXMsIGFuZCBvdXRzaWRlIHRoYXQgcmFuZ2UgaXQgcHJvZHVjZXMgYSBudW1iZXIgcmF0aGVyIHRoYW4gYSBwcmVkaWN0aW9uLiBPZnRlbiB0aGUgbnVtYmVyIGlzIGltcG9zc2libGUsIHdoaWNoIGlzIHRoZSBtb2RlbCB0ZWxsaW5nIHlvdSBzby4=',
     'V2hlcmUgZGlkIHRoZSBsaW5lIGdldCBpdHMgZXZpZGVuY2U/'),
    'w6_m5': ('3e23e8160039',
     'QWJvdXQgMC44Ny4gVGhlIFNEIG9mIHRoZSByZXNpZHVhbHMgaXMgdGhlIHNxdWFyZSByb290IG9mIG9uZSBtaW51cyByIHNxdWFyZWQsIHRpbWVzIHRoZSBTRCBvZiB5LCBzbyB0aGF0IHJvb3QgZXF1YWxzIDYuNSBvdmVyIDEzLjAsIHdoaWNoIGlzIDAuNS4gVGhlbiByIHNxdWFyZWQgaXMgMC43NSBhbmQgciBpcyBhYm91dCAwLjg2Ni4gVGhlIHNpZ24gY2Fubm90IGJlIHJlY292ZXJlZCBmcm9tIHRoZSBTRHMgYWxvbmUu',
     'V3JpdGUgZG93biB0aGUgaWRlbnRpdHksIHRoZW4gc29sdmUgaXQgZm9yIHIu'),
    'w7_m1': ('2e7d2c03a950',
     'QmVjYXVzZSBpdCBoYXMgYWxyZWFkeSBzZWVuIHRob3NlIGFuc3dlcnMuIEEgb25lLW5lYXJlc3QtbmVpZ2hib3VyIGNsYXNzaWZpZXIgc2NvcmVzIDEwMCUgb24gaXRzIG93biB0cmFpbmluZyBzZXQgYnkgZmluZGluZyBlYWNoIHBvaW50J3MgaWRlbnRpY2FsIHNlbGYsIHdoaWNoIHRlbGxzIHlvdSBub3RoaW5nIGF0IGFsbCBhYm91dCBuZXcgZGF0YS4=',
     'V2hhdCBkb2VzIHRoZSBjbGFzc2lmaWVyIGFscmVhZHkga25vdyBhYm91dCB0aG9zZSByb3dzPw=='),
    'w7_m2': ('ca978112ca1b',
     'Q29udmVydCB0aGUgYXR0cmlidXRlcyB0byBzdGFuZGFyZCB1bml0cyBmaXJzdC4gT3RoZXJ3aXNlIGFuIGF0dHJpYnV0ZSBtZWFzdXJlZCBpbiB0aG91c2FuZHMgZG9taW5hdGVzIHRoZSBkaXN0YW5jZSBjb21wbGV0ZWx5IGFuZCBvbmUgbWVhc3VyZWQgaW4gc2luZ2xlIGRpZ2l0cyBtaWdodCBhcyB3ZWxsIG5vdCBiZSB0aGVyZS4=',
     'RGlzdGFuY2UgYWRkcyB1cCBzcXVhcmVkIGRpZmZlcmVuY2VzLiBXaGljaCBhdHRyaWJ1dGUgY29udHJpYnV0ZXMgbW9zdD8='),
    'w7_m3': ('3e23e8160039',
     'QW4gZXZlbiBrIGNhbiB0aWUsIHdpdGggdGhlIHNhbWUgbnVtYmVyIG9mIG5laWdoYm91cnMgdm90aW5nIGVhY2ggd2F5LCBhbmQgdGhlIGNsYXNzaWZpZXIgdGhlbiBuZWVkcyBhbiBhcmJpdHJhcnkgcnVsZSB0byBicmVhayBpdC4gQW4gb2RkIGsgY2Fubm90IHRpZSBiZXR3ZWVuIHR3byBjbGFzc2VzLg==',
     'UGljdHVyZSBmb3VyIG5laWdoYm91cnMgc3BsaXQgdHdvIGFuZCB0d28u'),
    'w7_m4': ('18ac3e7343f0',
     'WW91IG5lZWQgdGhlIGJhc2VsaW5lOiBob3cgb2Z0ZW4geW91IHdvdWxkIGJlIHJpZ2h0IGJ5IGFsd2F5cyBndWVzc2luZyB0aGUgY29tbW9uZXN0IGNsYXNzLiBJZiA3NCUgb2YgdGhlIGRhdGEgaXMgb25lIGNsYXNzLCB0aGVuIDc2JSBoYXMgYm91Z2h0IHlvdSBhbG1vc3Qgbm90aGluZy4=',
     'Q29tcGFyZWQgd2l0aCB3aGF0PyBUaGF0IGlzIHRoZSB3aG9sZSBxdWVzdGlvbi4='),
    'w7_m5': ('2e7d2c03a950',
     'RGlzdGFuY2UgaXMgbWVhc3VyZWQgb24gdGhlIGF0dHJpYnV0ZXMgb25seS4gTGVhdmluZyB0aGUgY2xhc3MgY29sdW1uIGluIGVpdGhlciBjcmFzaGVzIG9uIGEgbm9uLW51bWVyaWNhbCB2YWx1ZSBvciwgd29yc2UsIHF1aWV0bHkgbGV0cyB0aGUgYW5zd2VyIGluZmx1ZW5jZSB0aGUgbWVhc3VyZW1lbnQgb2Ygc2ltaWxhcml0eSwgd2hpY2ggaXMgY2lyY3VsYXIu',
     'V2hpY2ggY29sdW1uIGlzIHRoZSB0aGluZyB5b3UgYXJlIHRyeWluZyB0byBwcmVkaWN0Pw=='),
}
